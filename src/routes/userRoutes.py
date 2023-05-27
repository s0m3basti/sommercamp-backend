from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from controller import userController
from database import Database
from schemas.userSchema import User, UserCreate, UserUpdate

router = APIRouter()


@router.get(path="/user/{user_id}", response_model=User)
def get_user(user_id: str, db=Depends(Database().get_db)):
    user = userController.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(404, "User not found!")
    return user


@router.get(path="/user", response_model=list[User])
def get_users(db=Depends(Database().get_db)):
    return userController.get_users(db=db)


@router.post(path="/user", response_model=User)
def create_user(user: UserCreate, db=Depends(Database().get_db)):
    if userController.get_user_by_username(
        db=db, username=user.username
    ) or userController.get_user_by_email(db=db, email=user.email):
        raise HTTPException(400, "User with username or email exists already!")

    return userController.create_user(db=db, user=user)


@router.put("/user/{user_id}", response_model=User)
def update_user(user_id: str, user: UserUpdate, db=Depends(Database().get_db)):
    if not userController.get_user_by_id(db=db, user_id=user_id):
        raise HTTPException(404, "User not found!")

    return userController.update_user(db=db, user_id=user_id, user=user)


@router.delete("/user/{user_id}", status_code=204)
def delete_user(user_id: str, db=Depends(Database().get_db)):
    if not userController.get_user_by_id(db=db, user_id=user_id):
        raise HTTPException(404, "User not found!")

    return userController.delete_user(db=db, user_id=user_id)
