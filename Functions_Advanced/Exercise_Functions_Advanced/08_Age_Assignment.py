def age_assignment(*args, **kwargs):
    person = {name:kwargs[name[0]]for name in args}
    # for name in args:
    #     person[name] = kwargs[name[0]]
    person = sorted(person.items())
    result = []
    for names,age in person:
        result.append(f"{names} is {age} years old.")
    return '\n'.join(result)



print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))