
with open("chutesAndLaddersBoard.txt", "r") as board:
    for line in board:
        tile = line.strip("\n").split(",")
        print(tile)