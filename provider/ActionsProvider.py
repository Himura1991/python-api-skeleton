from actions.GetUserAction import GetUserAction
from actions.InsertUserAction import InsertUserAction
from actions.GetAllUsersAction import GetAllUsersAction
from provider.RepositoryProvider import RepositoryProvider
from provider.SingletonMeta import SingletonMeta


class ActionsProvider(metaclass=SingletonMeta):
    def __init__(self):
        self.get_user_action = GetUserAction(RepositoryProvider().users)
        self.insert_user_action = InsertUserAction(RepositoryProvider().users)
        self.get_all_users_action = GetAllUsersAction(RepositoryProvider().users)
