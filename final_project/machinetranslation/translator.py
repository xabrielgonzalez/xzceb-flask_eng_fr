import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# initialize the language translator client
def init_language_translator():
    apikey = os.environ['apikey']
    url = os.environ['url']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2023-02-17',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    language_translator.set_disable_ssl_verification(True)
    return language_translator

language_translator = init_language_translator()

def english_to_french(text_to_translate):
    """This function translates an English text to French.
    Args:
        text_to_translate (str): the text to translate in English.
    Returns:
        french_text (str): the text translated in French.
    """
    translation = language_translator.translate(
        text=text_to_translate,
        source='en',
        target='fr'
    ).get_result()
    return translation['translations'][0]['translation']

def french_to_english(text_to_translate):
    """This function translates a French text to English.
    Args:
        text_to_translate (str): the text to translate in French.
    Returns:
        english_text (str): the text translated in English.
    """
    translation = language_translator.translate(
        text=text_to_translate,
        source='fr',
        target='en'
    ).get_result()
    return translation['translations'][0]['translation']

print(english_to_french('Hello everybody.'))
print(french_to_english('Bonjour'))
