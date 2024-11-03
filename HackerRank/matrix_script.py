import re

rows, cols = [int(x) for x in input().split()]
matrix = [input() for _ in range(rows)]





decoded_script = ''.join([''.join(row[i] for row in matrix) for i in range(cols)])
clean_text = re.sub(r'(?<=\w)(\W+)(?=\w)', ' ', decoded_script)


print(clean_text)
# input

# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!