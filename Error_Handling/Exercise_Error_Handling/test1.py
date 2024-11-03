import re

# Reading the matrix dimensions
rows, cols = map(int, input().split())

# Reading the matrix rows
matrix = [input() for _ in range(rows)]




decoded_script = ''.join([''.join(row[i] for row in matrix) for i in range(cols)])
clean_text = re.sub(r'(?<=\w)(\W+)(?=\w)', ' ', decoded_script)


print(clean_text)
