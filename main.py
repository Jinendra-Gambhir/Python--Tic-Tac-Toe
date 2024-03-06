# Import necessary modules
from tkinter import *
import random

# Function to handle the next turn in the game
def next_turn(row, column):

    global player

    # Check if the button is empty and the game is not won
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # If it's player 1's turn
        if player == players[0]:

            # Set the button text to player 1's symbol
            buttons[row][column]['text'] = player

            # Check for a winner or switch to player 2's turn
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            # If it's player 2's turn
            buttons[row][column]['text'] = player

            # Check for a winner or switch to player 1's turn
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

# Function to check if there is a winner
def check_winner():

    # Check each row for a winning combination
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Check each column for a winning combination
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check diagonals for a winning combination
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # Check for a tie
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

# Function to check for empty spaces on the board
def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

# Function to start a new game
def new_game():

    global player

    # Randomly choose starting player
    player = random.choice(players)

    # Set initial turn label
    label.config(text=player+" Turn")

    # Reset the board
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

# Create the main window
window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="grey")
window.geometry("1000x700")
window.resizable(False, False)
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# Create top frame for game title and label
top_frame = Frame(
    window,
    bg='#5D6D7E',
    width=1000,
    height=250
)
top_frame.place(x=0, y=0)

# Game title label
game_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text='Tic Tac Toe - By Jinendra',
    font=('', 42)
)
game_title.place(x=135, y=0)

# Label to display current player's turn
label = Label(top_frame, text=player + " Turn", font=('arial',30), bg = "#5D6D7E", fg ="white")
label.place(x=440,y= 200)

# Button to restart the game
reset_button = Button(top_frame, text="Restart Game", font=('arial',30),bg = "#5D6D7E", fg ="white", command=new_game)
reset_button.place(x=360, y=95)

# Create bottom frame for the game grid
bottom_frame = Frame(
    window,
    bg='#FFFFFF',
    width=400,
    height=400)
bottom_frame.place(x=265, y=300
)

# Create buttons for the game grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="",font=('consolas',40), width=5, height=1,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

# Run the main event loop
window.mainloop()

