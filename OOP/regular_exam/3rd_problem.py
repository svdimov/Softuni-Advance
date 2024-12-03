def list_roman_emperors(*args, **kwargs):
    success_imp = {}
    un_success_imp = {}


    for name, boolean in args:

        if name in kwargs:
            years = kwargs[name]
            if boolean:
                success_imp[name] = years
            else:
                un_success_imp[name] = years


    sorted_success_imp = sorted(success_imp.items(), key=lambda x: (-x[1], x[0]))

    sorted_unsuccess_imp = sorted(un_success_imp.items(), key=lambda x: (x[1], x[0]))



    totoal_imp = len(success_imp) + len(un_success_imp)
    result = [f"Total number of emperors: {totoal_imp}"]

    if sorted_success_imp:
        result.append("Successful emperors:")
        for name, years in sorted_success_imp:
            result.append(f"****{name}: {years}")


    if sorted_unsuccess_imp:
        result.append("Unsuccessful emperors:")
        for name, years in sorted_unsuccess_imp:
            result.append(f"****{name}: {years}")


    return "\n".join(result)


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14))
print('=============================')
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False),
                          ("Caligula", False), ("Pertinax", False), ("Vespasian", True),
                          Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19))
print('=========================')
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True),
                          Augustus=40, Trajan=19, Claudius=13))
