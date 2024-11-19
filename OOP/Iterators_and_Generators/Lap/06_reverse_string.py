def reverse_text (text:str):
    # my_list = [el for el in text][::-1]
    # rev_word = ''.join(my_list)
    # yield rev_word
    return text[::-1]


for char in reverse_text("step"):
    print(char, end='')