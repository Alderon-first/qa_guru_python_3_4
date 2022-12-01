# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.

import inspect

print("---------")


def print_inf_fnc(search_arg, arg_list, *args):
    i = 0
    search_arg = search_arg.__name__.capitalize().replace("_", " ")
    # получаю имя функции из параметра
    print(f"Имя функции:  {search_arg}")  # вывожу имя функции
    print("Аргументы функции :")
    for arg in args:
        # беру список args. arg отдает в печать новый элемент пока элементы не кончатмя
        # чтобы склеивать с именем использую индекс по массиву лист. предполагаю, что список аргументов, взятый из
        # из исходной функции всегда == по длинне списку знаечний агрументов, который я получаю как args,
        # хотя второй это картеж (кажется), а первый - массив
        print("--" + arg_list[i] + ": " + arg)
        i += 1  # увеличиваю счетчик
    print("-----------")


def open_browser(browser_name):
    arg_list = inspect.getfullargspec(open_browser).args  # тут получаю список аргументов в виде массива
    print_inf_fnc(open_browser, arg_list, browser_name)


def go_to_companyname_homepage(page_url):
    arg_list = inspect.getfullargspec(go_to_companyname_homepage).args
    # тут получаю список аргументов в виде массива
    print_inf_fnc(go_to_companyname_homepage, arg_list, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    arg_list = inspect.getfullargspec(find_registration_button_on_login_page).args
    # тут получаю список аргументов в виде массива
    print_inf_fnc(go_to_companyname_homepage, arg_list, page_url, button_text)


# -----
# работает, но не принято преподавателем
# def print_inf_fnc(fnc_name):
# for element in fnc:
# print("имя функции: " + element.__name__)
# print("атрибуты функции: " + str(inspect.signature(element))[1:-1])


# fnc = [find_registration_button_on_login_page, open_browser, go_to_companyname_homepage]
# print_inf_fnc(fnc)
# -----

open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://github.com")
find_registration_button_on_login_page(page_url="https://www.google.ru/", button_text="test")
