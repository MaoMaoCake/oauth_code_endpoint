from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/success")
async def success():
    return {"message": "yay"}


@app.get("/callback")
def callback(code: str):
    print(f"code: {code}")
    return {"Received Code": code}
