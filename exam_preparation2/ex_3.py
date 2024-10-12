

def accommodate(*guest_groups,**room_number ):

    rooms_sorted = sorted(room_number.items(),key=lambda kvp: (kvp[1], kvp[0]))
    accommodations = {}
    unsuccessful_accommodations = 0

    for guest in guest_groups:
        for room in rooms_sorted:
            if room[1] >= guest:
                accommodations[room[0][-3:]] = guest
                rooms_sorted.remove(room)
                break
        else:
            unsuccessful_accommodations += guest

    result = []
    if accommodations:
        result.append(f"A total of {len(accommodations)} accommodations were completed!")
        for room,guest in sorted(accommodations.items()):
            result.append(f"<Room {room} accommodates {guest} guests>")
    else:
        result.append("No accommodations were completed!")

    if unsuccessful_accommodations:
        result.append(f"Guests with no accommodation: {unsuccessful_accommodations}")

    if rooms_sorted:
        result.append(f"Empty rooms: {len(rooms_sorted)}")

    return '\n'.join(result)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print('========================================================')
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print('========================================================')
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))

