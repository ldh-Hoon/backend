import os
from data_control import *
from urls import *
import requests

def prepare(book):
    book_data = book_json(book)
    character_id_list = book_data['voice_id']
    for scene in book_data['script']:
        if scene['role']!='나레이션':
            with open(f"character/{character_id_list[scene['role']]}.wav", "rb") as f:
                raw = f.read()
            files = {'wav': raw}
            data = {'text': scene['text']}
            res = requests.post(TTS_ENDPOINT, files=files, data=data)
            with open(f'books/{book}/voices/{scene["id"]}.wav', 'wb') as file:
                file.write(res.content)
    data = {
        "status":"success"
    }

prepare("토끼와 거북이")
