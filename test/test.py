import requests
import base64
import io
import soundfile as sf
import librosa
import os
import winsound
import json

back = "172.23.245.219:8000"

#raw = open("paris.mp3", 'rb')
#res = requests.post(f'http://{back}/api/rvc/a1/토끼와 거북이/토끼', files={"file":raw})

#winsound.PlaySound(res.content, winsound.SND_MEMORY)

#res = requests.post(f'http://{back}/api/tts', json = {"id":"a1", "text":"토끼와 거북이", "role": "나레이션"})

#winsound.PlaySound(res.content, winsound.SND_MEMORY)

# request.post방식으로 파일전송.
#raw = encode_audio(files)
#res = requests.post('http://127.0.0.1:8000/account/update', json = {"id":"aaaa", "name":"김차차돌", "age":6, "gender":"m"})

res = requests.post(f'http://{back}/account/login', json={
  "email": "aaaa",
  "password": "bbbb"
})
print(res.json())

res = requests.post(f'http://{back}/account/register', json={
  "email": "a1",
  "password": "asd",
  "name" : "aaa1",
  "phoneNumber" : "01012394120",
  "age" : "5",
  "gender" : "men",
  "interests" : "a, r",
})
print(res.json())



res = requests.post(f'http://{back}/account/login', json={
  "email": "asasdd",
  "password": "asd"
})
print(res.json())

res = requests.get(f'http://{back}/account/get/su@gmail.com')
print(res.json())

#res = requests.post('http://172.23.245.219:8000/api/tts', json = {"email":"123","text":"너무 피곤하고 졸리다", "role":'나레이션'})
#print(res)
#winsound.PlaySound(res.content, winsound.SND_MEMORY)

#res = requests.post('http://127.0.0.1:8000/data/get', json = {"id":"a1", "type":"audio", "book":"토끼와 거북이", "file":"토끼"})
#print(res.content)

res = requests.get(f'http://{back}/data/booklist')
print(res.json())

#res = requests.post(f'http://{back}/data/get/file', json = {"id":"a1", "type":"json", "book":"토끼와 거북이", "file":"토끼"})
#data = res.content.decode('utf8').replace("'", '"')
#print(json.loads(data))


#res = requests.post(f'http://{back}/api/tts/prepare', json = {"id":"a1", "book":"토끼와 거북이"})
#print(res.json())

