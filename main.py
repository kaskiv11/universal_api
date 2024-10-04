from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def start_page():
    return {"message": "Hello World"}


