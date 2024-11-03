def getPosition(matrix, SearchValue):
    (x, y), = [(i, j) for i, row in enumerate(matrix)
               for j, element in enumerate(row)
               if element == SearchValue]
    return x, y


def aliceMove(matrix, x, y, moveDir, tea):
    directions = {
        "down": (1, 0),
        "up": (-1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    dx, dy = directions[moveDir]
    if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]):
        x += dx
        y += dy
        if matrix[x][y] == "R":
            matrix[x][y] = "*"
            return x, y, True, tea
        elif matrix[x][y] == "*" or matrix[x][y] == ".":
            matrix[x][y] = "*"
        else:
            tea += int(matrix[x][y])
            matrix[x][y] = "*"
    return x, y, False, tea


def main():
    # read
    matrix = []
    teaBags = 0
    rHole = False
    rows = int(input())
    for _ in range(rows):
        matrix.append(list(input().split()))

    # logic
    aliceX, aliceY = getPosition(matrix, "A")
    matrix[aliceX][aliceY] = "*"
    possibleCommands = ["up", "down", "right", "left"]

    while True:
        command = input()
        if command not in possibleCommands:
            continue
        aliceX, aliceY, rHole, teaBags = \
            aliceMove(matrix, aliceX, aliceY, command, teaBags)
        if rHole or teaBags >= 10:
            break

    # print
    if rHole or teaBags < 10:
        print("Alice didn't make it to the tea party.")
    else:
        print("She did it! She went to the party.")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
