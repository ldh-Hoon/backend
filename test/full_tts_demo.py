import requests
import base64
import io
import soundfile as sf
import librosa
import os
import json
import winsound
import speech_recognition as sr

back = "172.23.245.219:8000"

r = sr.Recognizer()
r.energy_threshold = 200
r.pause_threshold = 0.5
r.dynamic_energy_threshold = False

def mic_input():
    with sr.Microphone() as source:
        print("읽어주세요")
        audio = r.listen(source)

        return audio.get_wav_data()

book = "토끼와 거북이"
role = "a"
email = "a1"

#res = requests.post(f'http://{back}/api/tts/prepare', json = {"id":id, "book":book})
#print(res.json())

res = requests.post(f'http://{back}/data/get/file', json = {"email":email, "type":"json", "book":book,})
data = res.content.decode('utf8').replace("'", '"')
book_data = json.loads(data)


for scene in book_data['script']:
    now_scene = scene['id']
    print(f"{scene['role']} : {scene['text']}")
    
    if role == scene['role']:
        audio = mic_input()


    else:
        winsound.PlaySound(open(f"books/{book}/voices/{now_scene}.wav", "rb").read(), winsound.SND_MEMORY)
    
    print("___________________________\n")
