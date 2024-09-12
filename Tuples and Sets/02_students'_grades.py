m_dict = {}

for _ in range(int(input())):
    command = tuple(input().split())
    names, grades = command
    grades = float(grades)
    if names not in m_dict:
        m_dict[names] = []
    m_dict[names].append(grades)

for k,v in m_dict.items():
    avg = sum(v) / len(v)
    print(f"{k} -> {' '.join( [f'{x:.2f}' for x in v])} (avg: {avg:.2f})")

