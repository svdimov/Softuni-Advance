from functools import reduce
# редус използва ланда функция и колекция
m_list = [55,8,66,33]
sum_my_list = reduce(lambda x,y: x +y,m_list)
print(sum_my_list)