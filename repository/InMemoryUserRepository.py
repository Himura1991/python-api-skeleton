from domain.UserBase import User
from repository.UserRepository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self, db):
        self.db = db

    async def get_user(self, id_: int) -> User:
        return self.db[id_]

    async def insert(self, user: User) -> bool:
        self.db[max(self.db.keys())] = user
        return True

    async def get_all(self) -> dict[int, User]:
        return self.db

