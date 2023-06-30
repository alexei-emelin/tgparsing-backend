from typing import Sequence

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from services.payment.models import Payment


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
    session: AsyncSession, user_id: int | None = None
) -> Sequence[Payment]:
    stmt = sa.select(Payment)
    if user_id:
        stmt = stmt.where(Payment.user == user_id)
    result = await session.execute(stmt)
    payments = result.scalars().fetchall()
    return payments
