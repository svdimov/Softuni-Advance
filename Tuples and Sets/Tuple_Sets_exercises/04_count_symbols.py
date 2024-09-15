text = input()
times = sorted(set(text))

for ch in times:
    print(f"{ch}: {text.count(ch)} time/s")