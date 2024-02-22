from pydub import AudioSegment
from pydub.playback import play


def convert_aac2wav(email):
    sound = AudioSegment.from_file(f"parent/{email}.aac", "aac") 
    sound.export(f"parent/{email}.wav", format='wav')

#convert audio to datasegment

#sound = AudioSegment.from_file("parent/{email}.aac", "aac") 
#play(sound)

#sound.export("parent/{email}.wav", format='wav')


