from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/details")
async def details():
    return {"message": "Hello World", "details": "This is the details page"}