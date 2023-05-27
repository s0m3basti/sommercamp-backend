from sqlalchemy import CHAR, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from database import Database
from models.participantModel import Participant

Base = Database.Base


class Parent(Base):
    __tablename__ = "parents"

    id = Column(CHAR(32), primary_key=True, index=True)
    firstname = Column(String(255), index=True)
    participant_id = Column(CHAR(32), ForeignKey("participants.id"))

    participants = relationship(Participant, back_populates="participant")
