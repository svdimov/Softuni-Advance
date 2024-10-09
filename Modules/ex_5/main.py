from Modules.ex_5.fibo_seq import create_seq, locate_index

seq = None
while True:
    data = input()
    if data == "Stop":
        break

    if data.startswith("Create"):
        _,_,num = data.split()
        seq = create_seq(int(num))
        print(*seq)

    else:
        _,num_index = data.split()
        if seq is not None:
            try:
                idx = locate_index(seq,int(num_index))
                print(f"The number - {num_index} is at index {idx}")
            except ValueError:
                print(f"The number {num_index} is not in the sequence")
        else:
            print("Please first create sequence")

