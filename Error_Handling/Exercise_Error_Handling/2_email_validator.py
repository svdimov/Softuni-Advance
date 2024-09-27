class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGTH = 5
TLS_NAME = ['.com', '.bg', '.org', '.net']
while True:
    user = input()
    if user == 'End':
        break
    if '@' not in user:
        raise MustContainAtSymbolError('Email must contain @')

    user_name, domain = user.split('@')
    if len(user_name) < MIN_NAME_LENGTH:

        raise NameTooShortError("Name must be more than 4 characters")

    _, tls = domain.split('.')
    if f'.{tls}' not in TLS_NAME:
        raise  InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")



