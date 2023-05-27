import uuid

from sqlalchemy.orm import Session

from models import participantModel
from schemas import participantSchema


def get_participant(db: Session, participant_id: str):
    return (
        db.query(participantModel).filter(participantModel.id == participant_id).first()
    )


def create_participant(db: Session, participant: participantSchema.Participant):
    id = uuid.uuid4()

    db_user = participantModel.Participant(id=id, firstname=participant.firstname)

    db.add(db_user)
    db.commit()

    return db_user
