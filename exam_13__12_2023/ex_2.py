n = int(input())

game_board = []
gambler_pos = []
amount = 100
for r in range(n):
    game_board.append(list(input()))
    for c in range(n):
        if game_board[r][c] == "G":
            gambler_pos = [r, c]

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }

jackpot = False
while True:
    cmd = input()
    if cmd == "end":
        break
    new_r = gambler_pos[0] + directions[cmd][0]
    new_c = gambler_pos[1] + directions[cmd][1]

    if not (0 <= new_r < n and 0 <= new_c < n):
        print("Game over! You lost everything!")
        break

    game_board[gambler_pos[0]][gambler_pos[1]] = "-"

    if game_board[new_r][new_c] == "W":
        amount += 100


    elif game_board[new_r][new_c] == "P":
        amount -= 200
        if amount <= 0:
            amount = 0
            print("Game over! You lost everything!")
            break


    elif game_board[new_r][new_c] == "J":
        amount += 100000
        game_board[new_r][new_c] = "G"
        jackpot = True
        break
    gambler_pos = [new_r, new_c]
    game_board[gambler_pos[0]][gambler_pos[1]] = "G"

if jackpot:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {amount}$")
    for row in game_board:
        print(''.join(row))
elif amount > 0:
    print(f"End of the game. Total amount: {amount}$")
    for row in game_board:
        print(''.join(row))
