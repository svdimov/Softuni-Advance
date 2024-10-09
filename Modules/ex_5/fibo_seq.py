def create_seq(n):
    f_num = 0
    s_mum = 1

    fib_seq = [f_num,s_mum]

    for _ in range(2,n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def locate_index(fib_seq,number_index):
    return fib_seq.index(number_index)


