def draw_cards(*args, **kwargs):
    # Use dictionaries to store card names (key: card name, value: card type)
    monsters = {}
    spells = {}

    # Process tuple arguments (args)
    for card_name, card_type in args:
        if card_type == "monster":
            monsters[card_name] = card_type
        elif card_type == "spell":
            spells[card_name] = card_type

    # Process keyword arguments (kwargs)
    for card_name, card_type in kwargs.items():
        if card_type == "monster":
            monsters[card_name] = card_type
        elif card_type == "spell":
            spells[card_name] = card_type

    # Sort the monster and spell cards
    sorted_monsters = sorted(monsters.keys(), reverse=True)
    sorted_spells = sorted(spells.keys())

    # Prepare the result list
    result = []

    # Add monster cards if present
    if sorted_monsters:
        result.append("Monster cards:")
        for card in sorted_monsters:
            result.append(f"  ***{card}")

    # Add spell cards if present
    if sorted_spells:
        result.append("Spell cards:")
        for card in sorted_spells:
            result.append(f"  $$${card}")

    return "\n".join(result)

# print(draw_cards(("cyber dragon", "monster"),("cyber dragon", "monster"), freeze="spell", ))
# print('================================================================')
print(draw_cards(("celtic guardian", "monster"), \
                 ("earthquake", "spell"), \
                 ("fireball", "spell"), \
                 raigeki="spell", destroy="spell", ))
# print('=================================================================')
# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell", ))
