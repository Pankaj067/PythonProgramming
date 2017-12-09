# -*- coding: utf-8 -*-

from google.cloud import translate

def transalte_text(text,target='en'):
	translate_client = translate.Client()
	result = translate_client.translate(text, target_language=target)

	print("----------")

	print('Original Text: ', result['input'])

	print("----------")
	print('Transalation: ',result['translatedText'])

	print("----------")
	print('Detected source lang: ', result['detectedSourceLanguage'])


example_text = '''Hola saludos'''

transalte_text(example_text)
