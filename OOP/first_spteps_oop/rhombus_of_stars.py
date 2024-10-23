def print_row(space, star):
    print(" " * space + "* " * star)


def upper_stars(n):
    for row in range(1, n + 1):
        space = n - row
        print_row(space, row)


def button(n):
    for row in range(1, n):
        space = n - row
        print_row(row, space)


def rhombus(n):
    upper_stars(n)
    button(n)


n = int(input())
rhombus(n)
