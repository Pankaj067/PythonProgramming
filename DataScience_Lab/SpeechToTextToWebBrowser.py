import speech_recognition as rrs
import webbrowser as wb

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

r = rrs.Recognizer()

with rrs.Microphone() as source:
	print ("Let's Talk")
	audio = r.listen(source)
	print ("Got it!")

try: 
	text = r.recognize_google(audio)
	print("I think you said:\n"  + text)
	Httptext = "https://www.google.co.in/search?q=" + text

	wb.get(chrome_path).open(Httptext)

except Exception as e:
	print(e)