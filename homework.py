# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
import inspect


def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def print_inf_fnc(fnc_name):
    for element in fnc:
        print("имя функции: " + element.__name__)
        print("атрибуты функции: " + str(inspect.signature(element))[1:-1])


fnc = [find_registration_button_on_login_page, open_browser, go_to_companyname_homepage]
print_inf_fnc(fnc)
