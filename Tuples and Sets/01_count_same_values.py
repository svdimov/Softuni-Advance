number = tuple([float(el) for el in input().split()])

m_dict = {}

for num in number:
    m_dict[num] = number.count(num)

for k,v in m_dict.items():
    print(f"{k:.1f} - {v} times")