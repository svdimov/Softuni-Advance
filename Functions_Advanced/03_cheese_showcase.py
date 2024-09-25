from audioop import reverse


def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for k, v in sorted_cheeses:
        result += f"{k}\n"
        sort_list = sorted(v, reverse=True)
        result += "\n".join(str(x) for x in sort_list) + "\n"
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
