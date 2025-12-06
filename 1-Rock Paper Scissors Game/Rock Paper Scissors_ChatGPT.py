import tkinter as tk
from tkinter import messagebox
import random

score_win = 0
score_lose = 0
score_tie = 0

def update_score():
    score_label.config(text=f"Wins: {score_win} | Losses: {score_lose} | Ties: {score_tie}")


def on_enter(event, button):
    button.config(bg="#e6e6e6") 

def on_leave(event, button):
    button.config(bg="#f0f0f0") 

def on_click(event, button):
    button.config(bg="#d0d0d0")


def play_game(player_choice):
    global score_win, score_lose, score_tie
    
    choices = ['Rock', 'Paper', 'Scissors']
    
    computer_choice = random.choice(choices)

    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a tie!"
        score_tie += 1
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        score_win += 1
    else:
        result = "You lose!"
        score_lose += 1

    result_label.config(text=result)
    update_score()

def player_rock(event=None):
    play_game('Rock')

def player_paper(event=None):
    play_game('Paper')

def player_scissors(event=None):
    play_game('Scissors')

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("450x500")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24))
title_label.pack(pady=20)

score_label = tk.Label(root, text="Wins: 0 | Losses: 0 | Ties: 0", font=("Helvetica", 16))
score_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", font=("Helvetica", 14), command=player_rock, width=15, height=2)
rock_button.pack(pady=10)
rock_button.bind("<Enter>", lambda event, button=rock_button: on_enter(event, button))
rock_button.bind("<Leave>", lambda event, button=rock_button: on_leave(event, button))
rock_button.bind("<Button-1>", lambda event, button=rock_button: on_click(event, button))

paper_button = tk.Button(root, text="Paper", font=("Helvetica", 14), command=player_paper, width=15, height=2)
paper_button.pack(pady=10)
paper_button.bind("<Enter>", lambda event, button=paper_button: on_enter(event, button))
paper_button.bind("<Leave>", lambda event, button=paper_button: on_leave(event, button))
paper_button.bind("<Button-1>", lambda event, button=paper_button: on_click(event, button))

scissors_button = tk.Button(root, text="Scissors", font=("Helvetica", 14), command=player_scissors, width=15, height=2)
scissors_button.pack(pady=10)
scissors_button.bind("<Enter>", lambda event, button=scissors_button: on_enter(event, button))
scissors_button.bind("<Leave>", lambda event, button=scissors_button: on_leave(event, button))
scissors_button.bind("<Button-1>", lambda event, button=scissors_button: on_click(event, button))

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Helvetica", 14))
computer_choice_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 16, 'bold'))
result_label.pack(pady=20)

root.mainloop()
