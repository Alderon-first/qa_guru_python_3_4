# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
import traceback
import inspect

"""
def print_inf(имя исходной функции, аргументы исходной функции /*args/)
    аргументы_значения = переменная1.__name__.replace("_", " ").upper() + ":"
    print("Функция: " + переменная1 + "\n" + "Аргументы функции: " + переменная2)
    


def исходная функия (аргумент)
    переменная1 = взять меня исходной функции
    print_inf(переменная1, меременная2)
    
    исходная функия(аргумент=111)
    ----
    "Функция:  исходная функия
    "Аргументы функции: аргумент: 111
"""


def print_inf_fnc(search_arg, *args):
    search_arg = search_arg.__name__.replace("_", " ").upper() + ":"
    #не совсем то. Нужна конструкция, которая вернет "аргумент:значение"
    print("Имя функции:знаечние аргумента  -- "+ search_arg, *args)
    #print(name_fnc)


def open_browser(browser_name):
    global name_fnc
    name_fnc = inspect.currentframe().f_code.co_name
    #узнать имя текущей функции
    #тут нужно получить список аргументов, но пока не понятно как
    #print(name_fnc)
    print_inf_fnc(open_browser, browser_name) #считаю неправильным для каждой функции задачать аргументы здесь руками
    #А если их будет 500?? нужно подставить переменные вместо имени функции и списка аттребутов, чтобы они
    # #запрашивались и подставлялись сами
    #print_inf_fnc(name_fnc, browser_name)




def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass
#-----
#работает, но не принято преподавателем
#def print_inf_fnc(fnc_name):
    #for element in fnc:
        #print("имя функции: " + element.__name__)
        #print("атрибуты функции: " + str(inspect.signature(element))[1:-1])


#fnc = [find_registration_button_on_login_page, open_browser, go_to_companyname_homepage]
#print_inf_fnc(fnc)
#-----
open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="url")
find_registration_button_on_login_page(page_url="1", button_text="2")
