from fastapi import FastAPI

from routes.participantRoutes import router as participantsRouter
from routes.userRoutes import router as userRouter

app = FastAPI()

app.include_router(userRouter, tags=["user"])
app.include_router(participantsRouter, tags=["participants"])


@app.get("/")
def root():
    return {"HELLO WORLD"}


# TODO : add more models
