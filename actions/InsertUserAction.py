from repository.UserRepository import UserRepository
from domain.UserBase import User

class InsertUserAction:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def exec(self, user: User) -> bool:
        result: bool = await self.user_repository.insert(user)
        return result
