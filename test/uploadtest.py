import requests
import base64
import io
import soundfile as sf
import librosa
import os
import winsound

file = """C:\\Users\\2023-PC(T)-5\\Downloads\\Teemo.wav"""

back = "172.23.245.219:8000"

raw = open(file, 'rb')
res = requests.post(f'http://{back}/data/upload/parent_audio/123', files={"file":raw})
print(res)
