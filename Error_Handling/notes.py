
# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         break
#     except ValueError:
#         print("Ops! That was not valid number. Try again....")

#
# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         print(5/x)
#         break
#     except (ValueError,ZeroDivisionError):
#         print("Ops! That was not valid number. Try again....")
# finally block

# try:
#     print(int("5"))
#     print(5/0)
# except ValueError:
#     print('Invalid number')
# finally: # гаранция че минава винга  преб блока и дава грешка
#
#     print("print always")
# -----------------------try: else
# try:
#     print(int('5'))
#
# except ValueError:
#     print('Invalid number')
# else:
#     print('form else') #елсе се изпълнаява ако целия try: е бил успешен
# finally:
#
#     print("print always")
#------------------Custom Exception

# class CustomError(Exception):
#     pass
#
# raise  CustomError("My custom message")

# class ValueCannotBeNegative(Exception):
#     pass
# for _ in range(5):
#     number = int(input())
#     if number < 0:
#         raise ValueCannotBeNegative
 # ---------------any() all() different case :
# print(any([True,False])) # True like or
# print(all([True,False])) # False  like and
#-------server scan
# import time
# import socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(0.5)
# for i in range(1,256):
#     ip = f'151.251.126.{i}'
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.settimeout(0.5)
#         client_socket.connect((ip,7547))
#         print(f"server found {ip}")
#         break
#     except TimeoutError:
#         print(f" No conection to server adresa {ip}")
#     time.sleep(1)
#
#---------------barcode reader



