import random
import tkinter as tk
from tkinter import messagebox

def play(choice):
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    computer = random.choice([-1, 0, 1])
    you = youDict[choice]

    result_text = f"\nYou chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}\n"

    if computer == you:
        result_text += "\n🎯 It's a draw."
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result_text += "\n🏆 You Win!"
    else:
        result_text += "\n😞 You Lose!"
    
    custom_result_window(result_text)

def custom_result_window(result_text):
    result_win = tk.Toplevel()
    result_win.title("Game Result")
    result_win.geometry("400x250")
    result_win.configure(bg="#ffe4e1")
    
    tk.Label(result_win, text="Game Result", font=("Comic Sans MS", 22, "bold"), bg="#ffe4e1", fg="#d32f2f").pack(pady=10)
    tk.Label(result_win, text=result_text, font=("Arial", 16), bg="#ffe4e1", fg="#000").pack(pady=15)
    tk.Button(result_win, text="OK", command=result_win.destroy, bg="#388e3c", fg="white", font=("Arial", 14, "bold"), width=12).pack(pady=10)

# Create GUI
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("550x450")
root.configure(bg="#ffebf0")

frame = tk.Frame(root, bg="#fff8e1", padx=40, pady=40, relief=tk.RIDGE, borderwidth=8)
frame.pack(expand=True)

tk.Label(frame, text="🐍 Snake Water Gun 💧", font=("Comic Sans MS", 24, "bold"), bg="#fff8e1", fg="#8e24aa").pack(pady=20)

tk.Label(frame, text="Make Your Choice", font=("Arial", 16, "bold"), bg="#fff8e1", fg="#6a1b9a").pack(pady=15)

btn_snake = tk.Button(frame, text="🐍 Snake", command=lambda: play('s'), width=20, height=2, bg="#66bb6a", fg="white", font=("Arial", 14, "bold"))
btn_snake.pack(pady=10)

btn_water = tk.Button(frame, text="💧 Water", command=lambda: play('w'), width=20, height=2, bg="#42a5f5", fg="white", font=("Arial", 14, "bold"))
btn_water.pack(pady=10)

btn_gun = tk.Button(frame, text="🔫 Gun", command=lambda: play('g'), width=20, height=2, bg="#ef5350", fg="white", font=("Arial", 14, "bold"))
btn_gun.pack(pady=10)

root.mainloop()
