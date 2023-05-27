from pydantic import BaseModel


class ParticipantBase(BaseModel):
    firstname: str


class ParticipantCreate(ParticipantBase):
    pass


class Participant(ParticipantBase):
    id: str

    class Config:
        orm_mode = True
