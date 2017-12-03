import speech_recognition as rrs
import webbrowser as wb
import SpeechFile

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

r = rrs.Recognizer()

with rrs.Microphone() as source:
	print ("Let's Talk")
	audio = r.listen(source)
	print ("Got it!")

try: 
	text = r.recognize_google(audio)
	print(text)	
	lang='en'

	SpeechFile.tts(text,lang)
	Httptext = "https://www.google.co.in/search?q=" + text
	if text.find("Open") != -1 or text.find("open") != -1:
		wb.get(chrome_path).open(text[5:])
	else:
		wb.get(chrome_path).open(Httptext)

except Exception as e:
	print(e)