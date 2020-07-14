import hashlib
import  json
from datetime import datetime

def decor(fun):
    def wrapper(*args, **kwargs):
        dict_fun = {}
        dict_fun['дата'] = datetime.today()
        dict_fun['время вызова функции'] = datetime.now()
        dict_fun['аргументы функции'] = [args, kwargs]
        dict_fun['name_fun'] = fun.__name__
        result = fun(*args, **kwargs)

        with open('decorator.txt', 'w', encoding='utf-8') as file:
            for key, value in dict_fun.items():
                file.write(f'{key}: {value} \n')

        return result
    return wrapper


def generator(file):
    dict = {}
    counter = 1
    with open(file, encoding='utf-8') as fi:
        res = json.load(fi)
    for item in res:
        dict['country'] = item['country']
        hash_lib = hashlib.md5(b'item["url"]')
        dict['url'] = hash_lib.hexdigest()
        yield f'{counter}) {dict}'
        counter += 1


@decor
def coutry(file):
    for i in generator(file):
        print(i)

file = 'countru.json'

coutry(file)
