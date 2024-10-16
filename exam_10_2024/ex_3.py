def draw_cards(*m_card, **s_card):
    monsters = {}
    spells = {}
    for names, types in m_card:
        if types == "monster":
            monsters[names] = types
        elif types == "spell":
          spells[names] = types

    for names ,types in s_card.items():
        if types == "monster":
            monsters[names] = types

        elif types == "spell":
            spells[names] = types

    sorted_monsters = sorted(monsters.keys(), reverse=True)
    sorted_spells = sorted(spells.keys())


    result =[]

    if sorted_monsters:
        result.append("Monster cards:")
        for card in sorted_monsters:
            result.append(f"  ***{card}")

    if sorted_spells:
        result.append("Spell cards:")
        for spell in sorted_spells:
            result.append(f"  $$${spell}")

    return "\n".join(result)

#
# #
# print(draw_cards(("cyber dragon", "monster"),("cyber dragon", "monster"), freeze="spell", ))
# print('================================================================')
print(draw_cards(("celtic guardian", "monster"), \
                 ("earthquake", "spell"), \
                 ("fireball", "spell"), \
                 raigeki="spell", destroy="spell", ))
# print('=================================================================')
# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell", ))
