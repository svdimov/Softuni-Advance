

def rectangle(length, widht):
    if not isinstance(length, int) or not isinstance(widht, int):
        return "Enter valid values!"
    def area():
        result = length * widht
        return f"Rectangle area: {result}"

    def perimeter():
        result = 2 * (length + widht)
        return f"Rectangle perimeter: {result}"

    return f"{area()}\n{perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
