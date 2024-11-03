def read_lair():
    # Read dimensions of the matrix
    n, m = map(int, input().split())

    # Read the initial state of the matrix
    matrix = [list(input().strip()) for _ in range(n)]

    # Read the player's movement commands
    commands = input().strip()

    return n, m, matrix, commands


def find_player(matrix, n, m):
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 'P':
                return row, col
    return None


def spread_bunnies(matrix, n, m):
    # List of directions for bunny spread (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_bunnies = []

    # Identify all the cells currently occupied by bunnies
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 'B':
                new_bunnies.append((row, col))

    # Spread bunnies in all directions
    for bunny_row, bunny_col in new_bunnies:
        for dr, dc in directions:
            new_row, new_col = bunny_row + dr, bunny_col + dc
            if 0 <= new_row < n and 0 <= new_col < m:
                matrix[new_row][new_col] = 'B'


def is_player_dead(player_row, player_col, matrix):
    return matrix[player_row][player_col] == 'B'


def is_out_of_lair(player_row, player_col, n, m):
    return player_row < 0 or player_row >= n or player_col < 0 or player_col >= m


def simulate_game(n, m, matrix, commands):
    player_row, player_col = find_player(matrix, n, m)
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    for command in commands:
        # Move the player
        matrix[player_row][player_col] = '.'
        new_row, new_col = player_row + directions[command][0], player_col + directions[command][1]

        # Spread bunnies after each player move
        spread_bunnies(matrix, n, m)

        if is_out_of_lair(new_row, new_col, n, m):
            # Player wins by escaping the lair
            return matrix, "won", player_row, player_col

        # Update the player's position
        player_row, player_col = new_row, new_col

        if is_player_dead(player_row, player_col, matrix):
            # Player dies if they move into a bunny cell
            return matrix, "dead", player_row, player_col

        matrix[player_row][player_col] = 'P'

    # After processing all commands, check if the player is still alive or dead
    if is_player_dead(player_row, player_col, matrix):
        return matrix, "dead", player_row, player_col

    return matrix, None, player_row, player_col


def print_lair(matrix, n):
    for row in range(n):
        print(''.join(matrix[row]))


def main():
    n, m, lair, commands = read_lair()
    final_lair, result, final_row, final_col = simulate_game(n, m, lair, commands)

    print_lair(final_lair, n)

    if result == "won":
        print(f"won: {final_row} {final_col}")
    elif result == "dead":
        print(f"dead: {final_row} {final_col}")


if __name__ == "__main__":
    main()
