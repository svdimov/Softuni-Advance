
n, m = map(int, input().split())


matrix = [list(input().strip()) for _ in range(n)]


commands = input().strip()

player_row = 0
player_col = 0


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'P':
            player_row, player_col = i, j


directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

# Function to spread bunnies
def spread_bunnies(matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_bunnies = []

    # Identify the current bunnies
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 'B':
                new_bunnies.append((row, col))

    # Spread bunnies to adjacent cells
    for bunny_row, bunny_col in new_bunnies:
        for dr, dc in directions:
            new_row, new_col = bunny_row + dr, bunny_col + dc
            if 0 <= new_row < n and 0 <= new_col < m:
                matrix[new_row][new_col] = 'B'


# Simulate the game
game_over = False
for command in commands:
    # Move player
    matrix[player_row][player_col] = '.'
    new_row, new_col = player_row + directions[command][0], player_col + directions[command][1]

    # Spread bunnies after the player's move
    spread_bunnies(matrix)

    # Check if player is out of the lair
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
        game_over = True
        print('\n'.join(''.join(row) for row in matrix))
        print(f"won: {player_row} {player_col}")
        break

    # Update player's position
    player_row, player_col = new_row, new_col

    # Check if the player moves into a bunny
    if matrix[player_row][player_col] == 'B':
        game_over = True
        print('\n'.join(''.join(row) for row in matrix))
        print(f"dead: {player_row} {player_col}")
        break

    # Update the lair with the player's new position
    matrix[player_row][player_col] = 'P'

# Check the final state if all commands were executed
if not game_over:
    print('\n'.join(''.join(row) for row in matrix))
    if matrix[player_row][player_col] == 'B':
        print(f"dead: {player_row} {player_col}")
    else:
        print(f"won: {player_row} {player_col}")
