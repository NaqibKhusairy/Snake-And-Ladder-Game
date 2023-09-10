import tkinter as tk
import random

ROWS = 10
COLUMNS = 10
NUM_CELLS = ROWS * COLUMNS
PORTAL = {3, 5, 7, 9, 11, 14, 16, 18, 22, 25, 27, 30, 31, 36, 38, 42, 44, 47, 49, 51, 
53, 56, 60, 62, 64, 67, 71, 73, 75, 78, 80, 84, 87, 91, 93, 95, 97, 99}

PLAYER_COLORS = ["red", "blue", "green", "orange"]

root = tk.Tk()
root.title("Snake and Ladders")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

players = [0] * 4

# Load snake and ladder images
snake_image = tk.PhotoImage(file="src/portal.gif")
ladder_image = tk.PhotoImage(file="src/portal.gif")

def draw_board():
    cell_width = 40
    cell_height = 40

    for row in range(ROWS):
        for col in range(COLUMNS):
            x1, y1 = col * cell_width, row * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            cell_num = row * COLUMNS + col + 1

            if cell_num in PORTAL:
                canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=snake_image, tags="snakes")
            elif cell_num in PORTAL:
                canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=ladder_image, tags="ladders")
            
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(cell_num))

def roll_dice(player_position, player_index):
    result = random.randint(1, 6)
    result_label = result_labels[player_index]
    if({player_index} == {0}):
        plyr = 4
    else:
        plyr = player_index
    result_label.config(text=f"Player {plyr} Roll "+str(result))
    move_player(result, player_index)
    next_turn(player_index)

def move_player(steps, player_index):
    players[player_index] += steps
    if players[player_index] in SNAKES:
        players[player_index] = SNAKES[players[player_index]]
    elif players[player_index] in LADDERS:
        players[player_index] = LADDERS[players[player_index]]
    
    if players[player_index] >= NUM_CELLS:
        players[player_index] = NUM_CELLS  # Ensure the player doesn't go past the last cell
        result_label.config(text=f"Player {player_index + 1} wins!")

    update_player_position(player_index)

def update_player_position(player_index):
    canvas.delete(f"player{player_index}")
    cell_width = 40
    cell_height = 40
    cell_num = players[player_index] - 1

    row = cell_num // COLUMNS
    col = cell_num % COLUMNS

    x1, y1 = col * cell_width + 5, row * cell_height + 5
    x2, y2 = x1 + cell_width - 10, y1 + cell_height - 10

    canvas.create_oval(x1, y1, x2, y2, fill=PLAYER_COLORS[player_index], tags=f"player{player_index}")

def next_turn(current_player):
    roll_buttons[current_player].pack_forget()
    result_labels[current_player].pack_forget()
    current_player = (current_player + 1) % len(players)
    roll_buttons[current_player].pack()
    result_labels[current_player].pack()

roll_buttons = []
for i in range(len(players)):
    roll_buttons.append(tk.Button(root, text=f"Player {i + 1} Roll Dice", command=lambda i=i: roll_dice(players[i], i)))
    if i != 0:
        roll_buttons[i].pack_forget()
    else:
        roll_buttons[i].pack()

result_labels = []
for i in range(len(players)):
    result_labels.append(tk.Label(root, text=f"Dice: "))
    if i != 0:
        result_labels[i].pack_forget()
    else:
        result_labels[i].pack()

draw_board()
for i in range(len(players)):
    update_player_position(i)

current_player = 0

root.mainloop()