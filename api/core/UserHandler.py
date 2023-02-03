from fastapi import APIRouter
from domain.UserBase import User, UserBase
from provider.ActionsProvider import ActionsProvider

router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_users(user_id: int) -> User:
    return await ActionsProvider().get_user_action.exec(user_id)


@router.post("")
async def insert_users(user: UserBase) -> bool:
    return await ActionsProvider().insert_user_action.exec(user)


@router.get("")
async def get_all_users() -> list[User]:
    return await ActionsProvider().get_all_users_action.exec()

