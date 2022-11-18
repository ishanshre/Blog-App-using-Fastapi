from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Every thing is working fine"}