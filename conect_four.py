class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(ma):
    for el in ma:
        print(el)


def validate_column_choice(selected_column_num, max_index):
    if not (0 <= selected_column_num <= max_index):
        raise InvalidColumnError


def is_player_num(ma, r, c, player_n):
    if c < 0 or r < 0:
        return False
    try:
        if ma[r][c] == player_n:
            return True
    except IndexError:
        return False
    return False


def is_vertical_win(ma, r, c, player_n, slots):
    return all([is_player_num(ma, r + idx, c, player_n) for idx in range(slots)])


def is_horizontal_win(ma, r, c, player_n, slots):
    rights = []

    for idx in range(slots):
        if is_player_num(ma, r, c + idx, player_n):
            rights.append(True)
        else:
            break

    left = []

    for idx in range(slots):
        if is_player_num(ma, r, c - idx, player_n):
            left.append(True)
        else:
            break

    return len(left + rights) > slots


def is_right_diagonal(ma, r, c, player_n, slots):
    right_up = [is_player_num(ma, r - idx, c + idx, player_n) for idx in range(slots)].count(True)
    left_down = [is_player_num(ma, r + idx, c - idx, player_n) for idx in range(slots)].count(True)
    return (right_up + left_down) > slots


def is_left_diagonal(ma, r, c, player_n, slots):
    left_up = [is_player_num(ma, r - idx, c - idx, player_n) for idx in range(slots)].count(True)
    right_down = [is_player_num(ma, r + idx, c + idx, player_n) for idx in range(slots)].count(True)
    return (left_up + right_down) > slots


def is_winner(ma, r, c, player_n, slots=4):
    if any([
        is_vertical_win(ma, r, c, player_n, slots),
        is_horizontal_win(ma, r, c, player_n, slots),
        is_right_diagonal(ma, r, c, player_n, slots),
        is_left_diagonal(ma, r, c, player_n, slots)

    ]):
        return True
    return False


def place_player_choice(ma, selected_column_num, player_n):
    r_count = len(ma)
    for row_index in range(r_count - 1, -1, -1):
        curr_el = ma[row_index][selected_column_num]
        if curr_el == 0:
            ma[row_index][selected_column_num] = player_n
            return row_index, selected_column_num
    raise FullColumnError


row_count = 6
cols_count = 7

matrix = [[0 for _ in range(cols_count)] for _ in range(row_count)]

print_matrix(matrix)

player_num = 1
counter = 0

while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_num = int(input(f"Player {player_num} please chose a column: ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        row, col = place_player_choice(matrix, column_num, player_num)
        print_matrix(matrix)
        if is_winner(matrix, row, col, player_num, 4):
            print(f"The winner is player {player_num}")
            break
    except InvalidColumnError:
        print(f"Please select a number between 1 and {cols_count}")
        continue
    except FullColumnError:
        print("This column full! Please select another!")
        continue
    except ValueError:
        print("This is not a digit. Please select valid number!")
        continue
    counter += 1
    if row_count * cols_count == counter:
        print("The game is draw!")
        break
    player_num += 1
