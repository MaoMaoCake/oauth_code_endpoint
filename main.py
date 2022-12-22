from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/callback")
def callback(code: str):
    print(f"code: {code}")
    return code
