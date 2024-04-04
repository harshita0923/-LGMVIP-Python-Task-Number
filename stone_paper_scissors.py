import random

def get_user_choice():
    user_choice = input("Enter your choice (stone, paper, or scissors): ").lower()
    while user_choice not in ['stone', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter stone, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Stone Paper Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()








import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def play_again():
    result_label.config(text="")
    stone_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Stone Paper Scissors")

stone_button = tk.Button(root, text="Stone", command=lambda: play_game('stone'))
stone_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack()

root.mainloop()