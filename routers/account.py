from fastapi import APIRouter
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from utils.data_control import *
from fastapi.responses import JSONResponse, FileResponse


class Login_payload(BaseModel):
    email: str
    password: str

class Register_payload(BaseModel):
    password: str
    name: str
    email: str
    phoneNumber: str
    age: str
    gender: str
    interests: str
    
class Data_add_payload(BaseModel):
    password: str
    name: str
    email: str
    phoneNumber: str
    age: str
    gender: str
    interests: str

account = APIRouter(prefix='/account')

@account.post('/login')
async def login(data: Login_payload):
    if login_check(data.email, data.password):
        return "success"
    return "fail"

@account.post('/register')
async def register(data: Register_payload):
    if add_account(data.email, data.password, data.name):
        add_data(data.name, data.email, data.phoneNumber, data.interests, data.age, data.gender)
        return "success"
    return "fail"

@account.post('/update')
async def update(data: Data_add_payload):
    if add_data(data.name, data.email, data.phoneNumber, data.interests, data.age, data.gender):
        return "success"
    return "fail"

@account.get('/get/{user}')
async def get_data(user):
    data = get_json()
    if user in data:
        return JSONResponse(data[user]['info'])
    return "fail"


