import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

tk.Label(root, text="Choose your move:", font=("Helvetica", 14)).pack(pady=10)

tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

computer_label = tk.Label(root, text="", font=("Arial", 12))
computer_label.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()
