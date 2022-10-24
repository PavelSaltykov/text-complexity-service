import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def openapi():
    return app.openapi()


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
