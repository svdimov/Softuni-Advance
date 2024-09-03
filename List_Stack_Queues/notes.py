# STACKS LIFO*****
# num = [] #append добавя винаги последния
# num.append(5)
# num.append(10)
# num.append(4)
# print(num)
# num.pop() # премахва винаги последния елемент
# print(num)
#BIG O COMPLEXITY
#O(1) най бързият
# nums = [1,2.3]
# num = int(input())
# print(nums[0]) # is fast
# nums.insert(0,100) # is slower it is worst
# for el in nums:  #O(n) малко бавничко
#     if el == num:
#         print("found")

#Queues FIFO****** ОПАШКИ

# num = [1,2,3]
# num.pop(0) # worst scenario insert() too
# print(num)
from collections import deque
num = deque([1,2,3])
num.popleft()
print(num)