import random

snake = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 98: 78}
ladder = {3: 11, 22: 28, 42: 59, 49: 52, 66: 69, 76: 90, 83: 87, 88: 91, 90: 99}

def RollDice(player_num):
    print("-------------------------------------")
    input("Player " + str(player_num) + " Turn: Press Enter to Roll ")
    print("-------------------------------------")
    roll_num = random.randint(1, 6)
    print("You rolled: ", roll_num)
    return roll_num

BilPlayer = int(input("Please Insert The Number Of Players: "))
positions = {}

for player in range(1, BilPlayer + 1):
    positions[player] = 0

while True:
    for player in range(1, BilPlayer + 1):
        roll_num = RollDice(player)
        positions[player] += roll_num

        if positions[player] in snake:
            print("Player " + str(player) + " landed on a snake ")
            positions[player] = snake[positions[player]]
        elif positions[player] in ladder:
            print("Player " + str(player) + " landed on a ladder ")
            positions[player] = ladder[positions[player]]

        if positions[player] == 100:
            print("Player " + str(player) + " You Are Now At: " + str(positions[player]))
            print("Player " + str(player) + " has won!")
            exit()
        elif positions[player] > 100:
            extrapos = positions[player] - 100
            positions[player] = 100 - extrapos
        print("Player " + str(player) + " You Are Now At: " + str(positions[player]))