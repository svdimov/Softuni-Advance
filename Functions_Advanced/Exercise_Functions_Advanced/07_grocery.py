def grocery_store(**kwargs):
    recept = sorted(kwargs.items(),key=lambda kvp:(-kvp[1],-len(kvp[0]),kvp[0]))

    return "\n".join(f"{k}: {v}"for k,v in recept)





print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))