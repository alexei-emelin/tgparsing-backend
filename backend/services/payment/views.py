import fastapi as fa
from sqlalchemy.ext.asyncio import AsyncSession

import services.payment.db_handlers as db_hand
import services.payment.schemas as payment_schemas
from database.db_async import get_async_session
from services.payment.utils.robokassa import generate_payment_link
from services.user.dependencies import get_current_user


async def get_payment_link(
    schema: payment_schemas.PaymentCreate,
    user=fa.Depends(get_current_user),
    session: AsyncSession = fa.Depends(get_async_session),
) -> str:
    data = {
        "user": user.id,
        "amount": schema.amount,
        "action": payment_schemas.PaymentChoice.DEBIT,
    }
    payment = await db_hand.add_payment(session, data)
    url = generate_payment_link(payment.id, schema)
    return url