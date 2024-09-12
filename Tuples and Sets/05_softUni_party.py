all_guest = set()
for _ in range(int(input())):
    guest = input()
    all_guest.add(guest)

while True:
    enter_guest = input()
    if enter_guest == "END":
        break
    if enter_guest in all_guest:
        all_guest.remove(enter_guest)

print(len(all_guest))
print(*sorted(gst for gst in all_guest),sep='\n')




