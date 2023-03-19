from fastapi import FastAPI

app = FastAPI()
print("HELLO")

@app.get("/")
def root():
    return "Hello World!"