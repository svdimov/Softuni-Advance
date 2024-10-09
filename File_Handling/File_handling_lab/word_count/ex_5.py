import re
with open("words.txt") as file:
    words = file.read().split()

with open("text.txt") as file:
    content = file.read()

dict_ooc = {}

for word in words:
    pattern = re.compile(f"\\b({word})\\b", re.IGNORECASE)
    match = re.findall(pattern,content)

    dict_ooc[word] = len(match)
sort_dict = sorted(dict_ooc.items(), key=lambda kvp: -kvp[-1])
print(sort_dict)
with open("sort.txt", "w") as file:
    for k,v in sort_dict:
        file.write(f"{k} - {v}\n")