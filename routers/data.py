from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse, FileResponse

from utils.convert import *
from utils.data_control import *
import os

data_api = APIRouter(prefix='/data')

class File_request_payload(BaseModel):
    email: str
    type: str
    book: Optional[str] = None
    file: Optional[str] = None

@data_api.post("/upload/parent_audio/{email}")
async def upload_audio(file : UploadFile, email):
    content = await file.read()
    with open(f"parent/{email}.aac", 'wb') as file:
        file.write(content)
    convert_aac2wav(email)
    return "ok"

@data_api.get('/토끼')
async def show():
    return FileResponse("books/토끼와 거북이/img/토끼.png")

@data_api.get('/booklist')
async def booklist():
    books = os.listdir('./books')
    return JSONResponse({"books":books})


@data_api.post('/get/file')
async def return_file(payload : File_request_payload):
    if payload.type == "json":
        filepath = os.path.join("./books", payload.book, f"{payload.book}.json")
        if not os.path.isfile(filepath):
            return "fail"
        return FileResponse(filepath)
    
    
    elif payload.type == "image" and payload.book != None and payload.file != None:
        
        filepath = os.path.join("./books", payload.book, "img",f"{payload.file}.png")
        if not os.path.isfile(filepath):
            return "fail"
        
        return FileResponse(filepath)
    
    elif payload.type == "audio" and payload.book != None and payload.file != None:
        
        filepath = os.path.join("./books", payload.book, "voices", f"{payload.file}.wav")
        if not os.path.isfile(filepath):
            return "fail"
        
        return FileResponse(filepath)
    return 'fail'