# with open("text.txt", "r") as file :
#     for row,line in enumerate(file.readlines()):
#         if row % 2 == 0:
#             for ch in "-,.!?":
#                 line = line.replace(ch,"@")
#             print(' '.join(reversed(line.split())))






# import re
# with open("text.txt") as f:
#     line = f.readlines()
#     for i in range(0,len(line),2):
#         ln = reversed(re.sub("[-,.!?]" , "@", line[i]).split())
#         print(*ln)
