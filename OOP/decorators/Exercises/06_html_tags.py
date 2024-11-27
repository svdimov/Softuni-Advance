def tags(value):
    def decorator(func):
        def wrapper(*args):
            open_tag = f'<{value}>'
            close_tag = f"</{value}>"
            res = f"{open_tag}{func(*args)}{close_tag}"
            return res
        return wrapper
    return decorator





@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
print('===========================')
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))