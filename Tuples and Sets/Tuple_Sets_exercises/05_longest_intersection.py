def creat_set(range_str):
    start,end  = range_str.split(',')
    return set(range(int(start),int(end)+1))
longest_intersection_numbers = set()


for i in range(int(input())):
    f_r,s_r = input().split('-')
    # first_start,first_end = [int(x)for x in f_r.split(',')]
    # second_start,second_end = [int(x)for x in s_r.split(',')]

    first_set = creat_set(f_r)
    second_set = creat_set(s_r)

    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection_numbers):
        longest_intersection_numbers = intersection

print(f'Longest intersection is {list(longest_intersection_numbers)} with length {len(longest_intersection_numbers)}')


