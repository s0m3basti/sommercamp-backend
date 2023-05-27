from sqlalchemy import CHAR, Column, String

from database import Database

Base = Database.Base


class Participant(Base):
    __tablename__ = "participants"

    id = Column(CHAR(32), primary_key=True, index=True)
    firstname = Column(String(255), index=True)
