from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from routers.api import api
from routers.account import account
from routers.data import data_api


app = FastAPI()

app.include_router(api)
app.include_router(account)
app.include_router(data_api)


@app.get("/")
async def home():
    
    return "Hello!"

@app.get("/hello/{user}")
async def home(user):
    
    return f"Hello! {user}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = 8000)

