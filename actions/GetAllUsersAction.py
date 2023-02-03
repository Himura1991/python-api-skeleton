from repository.UserRepository import UserRepository
from domain.UserBase import User


class GetAllUsersAction:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def exec(self) -> dict[int, User]:
        return await self.user_repository.get_all()
