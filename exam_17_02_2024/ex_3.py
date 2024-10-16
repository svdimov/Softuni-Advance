def cookbook(*book):

    cuisine_dict = {}

    for recipe in book:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisine_dict.items(), key=lambda x: (-len(x[1]), x[0]))


    print_output = []

    for cuisine, dishes in sorted_cuisines:

        sorted_dishes = sorted(dishes, key=lambda x: x[0])
        recipe_count = len(sorted_dishes)

        print_output.append(f"{cuisine} cuisine contains {recipe_count} recipes:")
        for recipe_name, ingredients in sorted_dishes:
            ingredients_list = ', '.join(ingredients)
            print_output.append(f"  * {recipe_name} -> Ingredients: {ingredients_list}")

    return "\n".join(print_output)




print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))