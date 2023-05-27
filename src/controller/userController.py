import uuid

from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from models.userModel import User
from schemas.userSchema import UserCreate, UserUpdate


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    id = str(uuid.uuid4())
    password = bcrypt.hash(user.password)

    db_user = User(
        id=id,
        username=user.username,
        password=password,
        password_set=True,
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        rights=user.rights,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: str, user: UserUpdate):
    db.query(User).filter(User.id == user_id).update(
        {
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email,
            "rights": user.rights,
        }
    )

    db.commit()

    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: str):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return
