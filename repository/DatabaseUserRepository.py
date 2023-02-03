from domain.UserBase import UserCreate as DomainUserCreate, User
from provider.DatabaseProvider import async_session
from model.User import User as ModelUser
from sqlalchemy import select
from repository.UserRepository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession


class DatabaseUserRepository(UserRepository):
    def __init__(self):
        self.session: AsyncSession = async_session()

    async def get_user(self, id_: int):
        result = await self.session.execute(select(ModelUser).where(ModelUser.id == id_))
        return result.scalars().one()

    async def insert(self, user: DomainUserCreate) -> bool:
        try:
            new_user = ModelUser(name=user.name)
            self.session.add(new_user)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            return False

        return True

    async def get_all(self) -> dict[int, User]:
        result = await self.session.execute(select(ModelUser))
        return result.scalars().all()
