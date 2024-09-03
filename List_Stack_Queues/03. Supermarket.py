from collections import deque

def supermarket():
    my_deque = deque()

    while True:
        name = input()
        if name == "Paid":
            while len(my_deque):
                print(my_deque.popleft())
        elif name == "End":
            print(f"{len(my_deque)} people remaining.")
            break
        else:
            my_deque.append(name)

supermarket()
