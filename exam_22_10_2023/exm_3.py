def team_lineup(*args):
    football_players = {}

    for names, country in args:
        if country not in football_players:
            football_players[country] = [names]
        else:
            football_players[country] += [names]

    sorted_players = sorted(football_players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    resul = []
    for country, names in sorted_players:
        resul.append(f"{country}:")
        for name in names:
            resul.append(f"  -{name}")
    return '\n'.join(resul)


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
print('=========================')
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
print('============================')
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
