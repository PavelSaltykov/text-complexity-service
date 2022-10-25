from fastapi import FastAPI

app = FastAPI(title="text-complexity-service")


@app.get("/", include_in_schema=False)
async def openapi():
    return app.openapi()
