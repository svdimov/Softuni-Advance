# def uppercase(function):
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper
# Make Open/close principle in decorators functions
# def upper(function):
#
#     def wrapper(message):
#         res = function(message)
#         return res.upper()
#     return wrapper
# @upper
# def print_text(message):
#     return message
#
# print(print_text("test"))
# можем да извикваме функцията само ако искаме да бъде изълнена
# def vowel_filter(function):
#
#     def wrapper(should_be_trigger):
#         if should_be_trigger: # изпълнява се на True
#             res = function(should_be_trigger)
#             return [el for el in res if el.lower() in 'aiuoey' ]
#         return 'executed False for None'
#     return wrapper
#
#
# @vowel_filter
# def get_letters(should_be_trigger):
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters(True))
# print(get_letters(False))
# print(get_letters(False))

# връща докумнатацията на функцшята във декоратора
# from functools import wraps
# def vowel_filter(function):
#     @wraps(function)
#     def wrapper(should_be_trigger):
#         if should_be_trigger: # изпълнява се на True
#             res = function(should_be_trigger)
#             return [el for el in res if el.lower() in 'aiuoey' ]
#         return 'executed False for None'
#     return wrapper
#
#
# @vowel_filter
# def get_letters(should_be_trigger):
#     """Thi is my doc """
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters.__doc__)
# print(get_letters.__name__)


#   ------------args--------------


# from functools import wraps
#
#
# def vowel_filter(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         res = function(*args,**kwargs)
#         return [el for el in res if el.lower() in 'aiuoey']
#
#     return wrapper
#
#
# @vowel_filter
# def get_letters(char):
#     """Thi is my doc """
#     return char
# @vowel_filter
# def concat_letters(first_list,sec_list):
#     return first_list + sec_list
#
# print(get_letters(['a', 'b']))
# print(get_letters(['c,''d']))
# print(concat_letters(['a','v'],['i','d']))

# from time import time
# def measure_time(func):
#  def wrapper(*args,**kwargs):
#     start = time()
#     result = func(*args,**kwargs)
#     end = time()
#     print(end - start)
#     return result
#
#  return wrapper
# @measure_time
# def sum_nums(a,b):
#     return a+b
#
# print(sum_nums(5,6))

#    ------------------Passing Arguments-------------
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator
# @repeat(4)
# def say_hi():
#  print("Hello")
#
# say_hi()
#---------- няколко декората на една функция ------------

# def vowels(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return ''.join([el for el in res if el.lower() in 'aiuyo'])
#     return wrapper
#
# def upper(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res.upper()
#     return wrapper
#
#
# @upper
# @vowels
# def message(text):
#     return text
#
# print(message('stefani'))

#---------------Classes as Decorators--------------


# class func_logger:
#     _logfile = 'out.log'
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args):   # instead def wrapper()
#         log_string = self.func.__name__ + " was called"
#         with open(self._logfile, 'a') as opened_file:
#             opened_file.write(log_string + '\n')
#         return self.func(*args)
#
# @func_logger
# def say_hi(name):
#     print(f"Hi, {name}")

# @func_logger
# def say_bye(name):
#     print(f"Bye, {name}")
#
# say_hi("Peter")
# say_bye("Peter")


