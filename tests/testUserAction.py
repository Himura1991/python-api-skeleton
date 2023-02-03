import unittest

from repository.UserRepository import UserRepository
from repository.InMemoryUserRepository import InMemoryUserRepository
from actions.GetUserAction import GetUserAction
from actions.InsertUserAction import InsertUserAction
from actions.GetAllUsersAction import GetAllUsersAction
from domain.UserBase import User


class TestUserAction(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        user: User = User(name="Martin", id=1)

        user_repository: UserRepository = InMemoryUserRepository({1: user})

        self.get_user_action = GetUserAction(user_repository)
        self.insert_user_action = InsertUserAction(user_repository)
        self.get_all_users_action = GetAllUsersAction(user_repository)
    
    async def test_user_get(self):
        user: User = await self.get_user_action.exec(1)
        self.assertEqual(user.name, "Martin")

    async def test_user_insert(self):
        user: User = User(name="Florencia", id=2)
        result: bool = await self.insert_user_action.exec(user)
        self.assertEqual(True, result)

    async def test_user_get_all(self):
        users: dict[User] = await self.get_all_users_action.exec()
        self.assertEqual(len(users.keys()), 1)


if __name__ == '__main__':
    unittest.main()