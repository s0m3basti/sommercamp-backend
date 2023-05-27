from fastapi import Depends
from fastapi.routing import APIRouter

from controller.participantController import create_participant
from database import Database
from schemas.participantSchema import Participant, ParticipantCreate

router = APIRouter()


@router.post("/participant", response_model=Participant)
def create_user(participant: ParticipantCreate, db=Depends(Database().get_db)):
    return create_participant(db=db, participant=participant)
