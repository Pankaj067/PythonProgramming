import speech_recognition as sr

SpeechToText = sr.Recognizer()

with sr.Microphone() as source:
	print("Let's Talk!")
	audio = SpeechToText.listen(source)

try:
	print('I think you said:\n ' + SpeechToText.recognize_google(audio))

except: 
	pass