from fastapi import FastAPI

app = FastAPI(
    title="test",

)

@app.get("/test")
async def test():
    result = {"message": "Hello World"}
    return result
