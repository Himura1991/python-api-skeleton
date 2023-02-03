from domain.UserBase import User
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    async def get_user(self, id_: int) -> User:
        pass

    @abstractmethod
    async def insert(self, user: User) -> bool:
        pass

    @abstractmethod
    async def get_all(self) -> dict[int, User]:
        pass
