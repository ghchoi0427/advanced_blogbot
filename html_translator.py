from googletrans import Translator
from bs4 import BeautifulSoup


def local_translate(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    text_content = soup.get_text()

    translator = Translator()

    translated_text = translator.translate(text_content, src='en', dest='ko').text

    translated_html = html_content.replace(text_content, translated_text)

    return translated_html
