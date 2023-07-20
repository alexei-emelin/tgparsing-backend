import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from services.telegram.tasks.models import Task


async def create_task(session: AsyncSession, task_data: dict) -> Task:
    task = Task(**task_data)
    session.add(task)
    await session.commit()
    return task


async def update_task(
    session: AsyncSession, task_id, task_data: dict
) -> Task | None:
    stmt = (
        sa.update(Task)
        .where(Task.id == task_id)
        .values(**task_data)
        .returning(Task)
    )
    result = await session.execute(stmt)
    task = result.scalars().first()
    await session.commit()
    return task


async def get_task_by_filter(session: AsyncSession, data: dict) -> Task | None:
    stmt = (sa.select(Task).filter_by(**data))
    result = await session.execute(stmt)
    task = result.scalars().first()
    return task
