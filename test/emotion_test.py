import requests
import winsound

text = "거북이야, 너는 왜 그리 느리게 걸어 나처럼 빠르게 달리는 게 얼마나 재미있는지 알아?"

emo_list = ['즐거움', '보통', '슬픔', '분노']

for l in emo_list:
    file = f"character/emo_girl/{l}.wav"

    raw = open(file, 'rb')
    files = {'wav': raw}
    data = {'text': text}
    res = requests.post("http://172.23.245.219:5000/tts", files=files, data = data)

    with open(f'{l}.wav', 'wb') as file:
        file.write(res.content)
    winsound.PlaySound(res.content, winsound.SND_MEMORY)
