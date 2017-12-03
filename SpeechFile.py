from gtts import gTTS
import pyglet
import time, os


def tts(text, lang):
	file = gTTS(text = text, lang = lang)
	filename = 'C:/Users/pankaj.kumar1/Desktop/PythonLib/SpeechFile/Speech.mp3'
	file.save(filename)

	music = pyglet.media.load(filename, streaming = False)
	music.play()

	time.sleep(music.duration)
	os.remove(filename)
