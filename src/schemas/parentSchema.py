import uuid

from pydantic import BaseModel


class ParentBase(BaseModel):
    firstname: str
    """lastname: str
    street: str
    zip_code: str
    city: str
    tel_landline: str | None = None
    tel_mobile: str | None = None
    tel_business: str | None = None
    email: str
    member: bool = False """


class ParentCreate(ParentBase):
    pass


class Parent(ParentBase):
    id: uuid.UUID
    participant_id: uuid.UUID

    class Config:
        orm_mode = True
