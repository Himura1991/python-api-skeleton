from repository.DatabaseUserRepository import DatabaseUserRepository
from repository.InMemoryUserRepository import InMemoryUserRepository
from domain.UserBase import User
from provider.SingletonMeta import SingletonMeta
import os


class RepositoryProvider(metaclass=SingletonMeta):
    def __init__(self):
        if os.environ.get('TEST'):
            self.users = InMemoryUserRepository({1: User(id=1, name="Martin")})
        else:
            self.users = DatabaseUserRepository()
