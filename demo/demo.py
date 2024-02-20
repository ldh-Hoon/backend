import json
import os
import glob
import winsound
import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as img
import time

id = 'aaaa'

file_list = glob.glob("demo/jsons/*")
book_list = [x.split("jsons\\")[1].split(".json")[0] for x in file_list]

print(book_list)

while True:
    book = input()

    if not book in book_list:
        print("no book!")
        continue
    
    with open(file_list[book_list.index(book)], 'r', encoding='utf-8') as f:
        book_data = json.load(f)
    
    print("등장인물 선택")
    print(book_data['charactor'])
    s = input()
    while not (s in book_data['charactor']):
        s = input()
    role = book_data['charactor'].index(s)

    show_scene = 0
    now_scene = 0
    for scene in book_data['script']:
        now_scene = scene['id']
        for d in book_data['scene_data']:
            if d['scene'] <= now_scene:
                show_scene = d['scene']

        #background = img.imread(f"demo/img/{book}_{book_data['scene_data'][show_scene]['background']}.png")
        #plt.imshow(background)
        
        character_image = img.imread(f"demo/img/{book}_{book_data['charactor'][scene['role']]}.png")
        plt.imshow(character_image)

        plt.show()
        print(f"{book_data['charactor'][scene['role']]} : {scene['text']}")
        
        if role == scene['role']:
            pass
        else:
            res = requests.post('http://172.23.245.219:8000/api/tts', json = {"id":id,"text":scene['text'], "role":book_data['charactor'][scene['role']]}).json()
            
            winsound.PlaySound(base64.b64decode(res['data']), winsound.SND_MEMORY)
