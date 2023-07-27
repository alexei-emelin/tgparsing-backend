from typing import Sequence

import sqlalchemy as sa
from services.payment.models import Payment
from sqlalchemy.ext.asyncio import AsyncSession


async def add_payment(session: AsyncSession, data: dict) -> Payment:
    payment = Payment(**data)
    session.add(payment)
    await session.commit()
    return payment


async def upd_payment(session: AsyncSession, id_row: int) -> Payment | None:
    stmt = (
        sa.update(Payment)
        .values({"status": True})
        .returning(Payment)
        .where(Payment.id == id_row)
    )
    result = await session.execute(stmt)
    payment = result.scalars().first()
    await session.commit()
    return payment


async def get_payments(
    session: AsyncSession,
    data: dict,
) -> Sequence[Payment] | None:
    stmt = sa.select(Payment)
    period_start = data.pop("period_start", None)
    period_end = data.pop("period_end", None)
    if period_start and period_end:
        stmt = stmt.where(Payment.date.between(period_start, period_end))
    for key, value in data.items():
        stmt = stmt.where(getattr(Payment, key) == value)
    result = await session.execute(stmt)
    payments = result.scalars().fetchall()
    return payments