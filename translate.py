import requests

KEY = 'trnsl.1.1.20181019T004137Z.1b33044816da2dde.98797f710dc87da22ab4b3a24621a519a4dfa2af'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_me(mytext):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
         & text=<переводимый текст>
         & lang=<направление перевода>
         & [format=<формат текста>]
         & [options=<опции перевода>]
         & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    params = {
        'key': KEY,
        'text': mytext,
        'lang': 'ru-fr'
    }
    response = requests.get(URL, params=params)
    return response.json()


json = translate_me('Привет, друг!')

print(json['text'][0])