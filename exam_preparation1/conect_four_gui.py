import tkinter as tk
from tkinter import messagebox

class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


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


class ConnectFourGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")


        self.row_count = 6
        self.cols_count = 7
        self.player_num = 1
        self.counter = 0
        self.matrix = [[0 for _ in range(self.cols_count)] for _ in range(self.row_count)]

        #
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=1, column=0)


        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=0, column=0)


        self.column_buttons = []
        for col in range(self.cols_count):
            button = tk.Button(self.buttons_frame, text=f"Drop {col + 1}", command=lambda col=col: self.on_column_click(col))
            button.grid(row=0, column=col)
            self.column_buttons.append(button)


        self.board_labels = [[tk.Label(self.board_frame, width=4, height=2, borderwidth=2, relief="groove", font=("Arial", 20)) for _ in range(self.cols_count)] for _ in range(self.row_count)]
        for r in range(self.row_count):
            for c in range(self.cols_count):
                self.board_labels[r][c].grid(row=r, column=c)

    def on_column_click(self, col):
        try:
            validate_column_choice(col, self.cols_count - 1)
            row, _ = place_player_choice(self.matrix, col, self.player_num)
            self.update_board()
            if is_winner(self.matrix, row, col, self.player_num, 4):
                messagebox.showinfo("Game Over", f"The winner is player {self.player_num}")
                self.reset_game()
            else:
                self.player_num = 2 if self.player_num == 1 else 1
                self.counter += 1
                if self.counter == self.row_count * self.cols_count:
                    messagebox.showinfo("Game Over", "The game is a draw!")
                    self.reset_game()
        except InvalidColumnError:
            messagebox.showwarning("Invalid Move", "Please select a valid column.")
        except FullColumnError:
            messagebox.showwarning("Full Column", "This column is full, please select another column.")

    def update_board(self):

        for r in range(self.row_count):
            for c in range(self.cols_count):
                if self.matrix[r][c] == 1:
                    self.board_labels[r][c].config(text="X", bg="red")
                elif self.matrix[r][c] == 2:
                    self.board_labels[r][c].config(text="O", bg="yellow")
                else:
                    self.board_labels[r][c].config(text="")

    def reset_game(self):
        # Reset the game state
        self.matrix = [[0 for _ in range(self.cols_count)] for _ in range(self.row_count)]
        self.player_num = 1
        self.counter = 0
        self.update_board()



if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFourGame(root)
    root.mainloop()
