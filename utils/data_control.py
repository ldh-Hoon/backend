import os.path
import json
import base64
import librosa
import soundfile as sf
import io

def down_sample(path, y, sr, resample_sr):
    resample = librosa.resample(y, orig_sr=sr, target_sr=resample_sr)
    sf.write(f'{path}.wav', resample, resample_sr, format='WAV', endian='LITTLE', subtype='PCM_16')
    return resample

def update(data):
    file = 'account.json' 

    if not os.path.isfile(file):
        json_data = {
            "aaaa" : {
                "pw" : "bbbb",
                "info" : {
                    "name" : "김차돌",
                    "phoneNumber" : None,
                    "age" : None,
                    "gender" : None,
                    "interests" : None,
                    "history" : None,
                }
            }
        }
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent="\t", ensure_ascii=False)
    
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent="\t", ensure_ascii=False)
    return 0

def get_json():
    file = 'account.json'

    if not os.path.isfile(file):
        json_data = {
            "aaaa" : {
                "pw" : "bbbb",
                "info" : {
                    "name" : "김차돌",
                    "phoneNumber" : None,
                    "age" : None,
                    "gender" : None,
                    "interests" : None,
                    "history" : None,
                }
            }
        }
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent="\t", ensure_ascii=False)
    else:
        with open(file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    return json_data

def book_json(book):
    file = f'./books/{book}/{book}.json'
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

def login_check(email, password): # 로그인 검증
    data = get_json()
    if email in data:
        if data[email]["pw"] == password:
            return True
    return False

def add_account(email, password, name): #  계정 추가
    data = get_json()

    if id in data:
        return False
    data[email]={
            "pw" : password,
            "info" : {
                "name" : name,
                "phoneNumber" : None,
                "age" : None,
                "gender" : None,
                "interests" : None,
                "history" : None,
            }
    }
    update(data)
    return True

def add_data(name, email, phoneNumber, interests, age, gender):
    data = get_json()

    if not email in data:
        return False
    data[email]={
            "pw" : data[email]["pw"],
            "info" : {
                "name" : name,
                "phoneNumber" : phoneNumber,
                "age" : age,
                "gender" : gender,
                "interests" : interests,
                "history" : None,
            }
    }
    update(data)
    return True