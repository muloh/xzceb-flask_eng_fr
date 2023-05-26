from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_Key = "hIvcDk97_DDGuzJPlkFvRKDumeHyuvvj_AOuE7ym03vO"
url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/ccde3f79-5c77-4fee-9655-1217e07e7635"

# Authenticate
authenticator = IAMAuthenticator(api_Key)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

translation = lt.translate(text="Hello World", model_id='en-de').get_result()
print(translation)
print(" ")

# extract the translation text 
print("========Translated Text ===========")
extracted_text = translation['translations'][0]['translation']
print(extracted_text)
print(" ")
 
# Identify Language 
language_identified = lt.identify("This is a regualar sentence").get_result()
print(language_identified)


# ============================ File 2==============================
# AI Travel Guide Text to speech 

from ibm_watson import TextToSpeechV1
tts_api_key = ""
tts_url = ""

#Authenticate
ttsauthenticator = IAMAuthenticator(tts_api_key)
tts = TextToSpeechV1(authenticator = ttsauthenticator)
tts.set_service_url(tts_url)

translation = lt.translate(text='We are sinking! Please send help', model_id='en-de').get_result()
text = translation['translations'][0][translation]
print(text)
# convert text to speech

with open('./help.mp3', 'wb') as audio_file:
	res = tts.synthesize(text, accept='audio/mp3', voice = 'de-DE_BirgitV3Voice').get_result()
	audio_file.write(res.content) #this generate an audio file with translated text 
