import tkinter as tk
from tkinter import messagebox
import winsound

def check_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    return None

def reset_board():
    global current_player, game_board
    current_player = "X"
    game_board = [["" for _ in range(3)] for _ in range(3)]
    update_board()

def reset_all_board():
    global current_player, game_board, x_win_count, o_win_count
    x_win_count = 0
    o_win_count = 0
    current_player = "X"
    game_board = [["" for _ in range(3)] for _ in range(3)]
    update_board()

def update_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=game_board[i][j])
    
    x_win_label.config(text=f"X Wins: {x_win_count}")
    o_win_label.config(text=f"O Wins: {o_win_count}")
def play_sound(sound):
    winsound.PlaySound(sound, winsound.SND_FILENAME)

def click(row, col):
    global current_player, game_board, x_win_count, o_win_count
    if game_board[row][col] == "":
        game_board[row][col] = current_player
        update_board()

        winner = check_winner(game_board)
        if winner:
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            if winner == 'X':
                x_win_count += 1
                x_win_label.config(text=f"X Wins: {x_win_count}")
                play_sound("tic_tac_toe/win_sound.wav")
            elif winner == 'O':
                o_win_count += 1
                o_win_label.config(text=f"O Wins: {o_win_count}")
                play_sound("tic_tac_toe/win_sound.wav")
            update_board()
            reset_board()
        elif all(all(cell != "" for cell in row) for row in game_board):
            messagebox.showinfo("Tie", "It's a tie!")
            play_sound("tic_tac_toe/tie_sound.wav")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

#I sware to God it's A GUI setup

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

game_board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

x_win_count = 0
o_win_count = 0

x_win_label = tk.Label(root, text=f"X Wins: {x_win_count}")
x_win_label.grid(row=0, column=1)

o_win_label = tk.Label(root, text=f"O Wins: {o_win_count}")
o_win_label.grid(row=1, column=1)

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=8, height=5, command=lambda row=i, col=j: click(row, col))
        buttons[i][j].grid(row=i+2, column=j)

reset_button = tk.Button(root, text="Reset", command=reset_board)
reset_button.grid(row=5, column=0)

reset_button = tk.Button(root, text="Reset All", command=reset_all_board)
reset_button.grid(row=5, column=1)

root.mainloop()