# import json
# import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from dotenv import load_dotenv

# load_dotenv()

# apikey = os.environ['apikey']
# url = os.environ['url']

APIKEY = "hIvcDk97_DDGuzJPlkFvRKDumeHyuvvj_AOuE7ym03vO"
URL = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/ccde3f79-5c77-4fee-9655-1217e07e7635"



authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url(URL)

# translation = language_translator.translate(
#text='Hello, how are you today?',
# model_id='en-es').get_result()

def english_to_french(english_text):
    #write the code here
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    translated_text = french_text['translations'][0]['translation']
    print(translated_text)
    return translated_text

# english_to_french("How are you doing?")


def french_to_english(french_text):
    #write the code here
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    translated_text = english_text['translations'][0]['translation']
    print(translated_text)
    return translated_text


# french_to_english("Comment ça va?")
