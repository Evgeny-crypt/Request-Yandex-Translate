import requests
from pprint import pprint
import os

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_file_path, to_file_path, to_lang='ru'):
    with open(from_file_path, encoding='utf-8') as initial_file:
        text = initial_file.read()
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': to_lang,
        'options': 1
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    pprint(json_['lang'])
    line = ''.join(json_['text'])

    with open(to_file_path, 'w') as file_output:
        file_output.write(line)


translate_it('DE.txt', 'DE_tr.txt')
translate_it('FR.txt', 'FR_tr.txt')
translate_it('ES.txt', 'ES_tr.txt')


def merge():
    print('Перемещаем перевод всех трех файлов в один текстовый файл <translate_DE_FR_ES>')
    merges = []
    for path in ['DE_tr.txt', 'FR_tr.txt', 'ES_tr.txt']:
        with open(path) as file_translate:
            merges.append(file_translate.read())
            merges.append('\n')

    with open('translate_DE_FR_ES.txt', 'w') as file_translate:
        for save in merges:
            file_translate.write(save)


merge()


def delete():
    for file_path in ['DE_tr.txt', 'FR_tr.txt', 'ES_tr.txt']:
        os.remove(file_path)


delete()
