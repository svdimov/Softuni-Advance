def draw_cards(*m_card, **s_card):

    monsters = []
    spells = []
    for names, types in m_card:
        if types == "monster":
            monsters.append(names)
        elif types == "spell":
            spells.append(names)
    for names, types in s_card.items():
        if types == "monster":
            monsters.append(names)
        elif types == "spell":
            spells.append(names)


    monsters.sort(reverse=True)
    spells.sort()
    result =[]

    if monsters:
        result.append("Monster cards:")
        for card in monsters:
            result.append(f"  ***{card}")

    if spells:
        result.append("Spell cards:")
        for spell in spells:
            result.append(f"  $$${spell}")

    return "\n".join(result)




print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print('-------------------------------------------------------')
print(draw_cards(("celtic guardian", "monster"),("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print('-------------------------------------------------')
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))