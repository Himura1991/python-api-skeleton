from repository.UserRepository import UserRepository
from domain.UserBase import User


class GetUserAction:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def exec(self, id_: int) -> User:
        return await self.user_repository.get_user(id_)