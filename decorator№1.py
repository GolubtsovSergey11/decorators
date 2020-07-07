from datetime import datetime

def decor(fun):
    def wrapper(*args, **kwargs):
        dict_fun = {}
        dict_fun['дата'] = datetime.today()
        dict_fun['аргументы функции'] = [args, kwargs]
        dict_fun['name_fun'] = fun.__name__
        fun(*args, **kwargs)

        with open('decorator.txt', 'w', encoding='utf-8') as file:
            for key, value in dict_fun.items():
                file.write(f'{key}: {value} \n')

        return fun
    return wrapper

@decor
def myltiplay(a, b):
    return a * b

print(myltiplay(2, 5))
