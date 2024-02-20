import os, requests
from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from utils.data_control import *
from fastapi.responses import Response, FileResponse, JSONResponse
from utils.urls import *
import glob

standard_wav = "parent/a1.wav"
api = APIRouter(prefix='/api')

class TTS_payload(BaseModel):
    email: str
    text: str
    role: str

class TTS_parent_payload(BaseModel):
    email: str
    book: str

class STT_payload(BaseModel):
    email: str
    text: str

@api.post('/tts')
async def TTS(data : TTS_payload):
    json_data = get_json()

    if not data.email in json_data:
        return "no email"

    if data.role == '나레이션':
        file = standard_wav
        if os.path.isfile(f"parent/{data.email}.wav"):
            file = f"parent/{data.email}.wav"

        raw = open(file, 'rb')
        files = {'wav': raw}
        data = {'text': data.text}
        res = requests.post(TTS_ENDPOINT, files=files, data = data)
        with open(f'temp.wav', 'wb') as file:
            file.write(res.content)
        return FileResponse("temp.wav", media_type="audio/wav")
    else:
        file_list = glob.glob("character/*.wav")
        voice_list = [x.split("character\\")[1].split(".wav")[0] for x in file_list]
        if not data.role in voice_list:
            raw = open(standard_wav, 'rb')
        else:
            raw = open(file_list[voice_list.index(data.role)], 'rb')
        files = {'wav': raw}
        data = {'text': data.text}
        res = requests.post(TTS_ENDPOINT, files=files, data = data)

        with open(f'temp.wav', 'wb') as file:
            file.write(res.content)
        return FileResponse("temp.wav", media_type="audio/wav")
        

@api.post('/tts/prepare')
async def prepare(data : TTS_parent_payload):
    json_data = get_json()

    if not data.email in json_data:
        return 'fail'

    file = f"parent/a1.wav"
    if os.path.isfile(f"parent/{data.email}.wav"):
        file = f"parent/{data.email}.wav"
    with open(file, 'rb') as f:
        raw = f.read()
    book_data = book_json(data.book)
    for scene in book_data['script']:
        if scene['role']=='나레이션':
            files = {'wav': raw}
            d = {'text': scene['text']}
            res = requests.post(TTS_ENDPOINT, files=files, data=d)
            with open(f'books/{data.book}/voices/{scene["email"]}.wav', 'wb') as file:
                file.write(res.content)

    data = {
        "status":"success"
    }

    return JSONResponse(data)

@api.post('/rvc/{email}/{book}/{role}')
async def prepare(file : UploadFile, email, book, role):
    raw = await file.read()
    json_data = get_json()
    age = json_data[email]['info']['age']
    gender = json_data[email]['info']['gender']
    if age==None:
        age = 7
    if gender==None:
        gender = 0
    
    books = os.listdir('./books')
    if not book in books:
        return "fail"
    characteremail = book_json(book)['voice_id'][role]

    files = {'wav': raw}
    data = {'CharacterId': characterId,
            'age': age,
            'gender': gender}
    requests.post(f'{RVC_ENDPOINT}/upload', files=files, data=data)

    response = requests.get(f'{RVC_ENDPOINT}/download')
    with open(f'temp.wav', 'wb') as file:
        file.write(response.content)
    
    return FileResponse('temp.wav')