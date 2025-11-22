import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game - KivroSolutions")
        self.root.configure(bg="#cbe8f6")

        # Make window full-screen
        self.root.attributes('-fullscreen', True)

        # Bind ESC to exit full-screen
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Random secret number
        self.secret_number = random.randint(1, 10)

        # --- Main Frame ---
        self.frame = tk.Frame(root, bg="#cbe8f6")
        self.frame.pack(expand=True)

        # --- Title Label ---
        tk.Label(
            self.frame,
            text="🎯 KivroSolutions Number Guessing Game 🎯",
            font=("Segoe UI", 36, "bold"),
            bg="#cbe8f6",
            fg="#005a9e",
        ).pack(pady=40)

        # --- Instructions ---
        tk.Label(
            self.frame,
            text="I'm thinking of a number between 1 and 10.\nCan you guess it?",
            font=("Segoe UI", 20),
            bg="#cbe8f6",
            fg="#333",
        ).pack(pady=20)

        # --- Entry Box ---
        self.entry = tk.Entry(
            self.frame, font=("Segoe UI", 20), justify="center", width=8, bd=2, relief="solid"
        )
        self.entry.pack(pady=20)

        # --- Buttons Frame ---
        btn_frame = tk.Frame(self.frame, bg="#cbe8f6")
        btn_frame.pack(pady=20)

        # Guess Button
        tk.Button(
            btn_frame,
            text="✅ Check Guess",
            font=("Segoe UI", 18, "bold"),
            bg="#007acc",
            fg="white",
            activebackground="#005a9e",
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=10,
            command=self.check_guess,
        ).grid(row=0, column=0, padx=10)

        # Restart Button
        tk.Button(
            btn_frame,
            text="🔄 Restart Game",
            font=("Segoe UI", 18, "bold"),
            bg="#f0ad4e",
            fg="white",
            activebackground="#d98c1a",
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=10,
            command=self.restart_game,
        ).grid(row=0, column=1, padx=10)

        # Exit Button
        tk.Button(
            btn_frame,
            text="❌ Exit",
            font=("Segoe UI", 18, "bold"),
            bg="#dc3545",
            fg="white",
            activebackground="#b02a37",
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=10,
            command=self.root.destroy,
        ).grid(row=0, column=2, padx=10)

        # --- Result Label ---
        self.result_label = tk.Label(
            self.frame, text="", font=("Segoe UI", 22, "bold"), bg="#cbe8f6", fg="#333"
        )
        self.result_label.pack(pady=30)

        # --- Footer ---
        tk.Label(
            self.frame,
            text="Press ESC to exit full screen",
            font=("Segoe UI", 12),
            bg="#cbe8f6",
            fg="#555",
        ).pack(side="bottom", pady=10)

    def check_guess(self):
        guess = self.entry.get().strip()
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 10.")
            return

        guess = int(guess)
        if guess < 1 or guess > 10:
            self.result_label.config(text="⚠️ Guess between 1 and 10 only!", fg="#d9534f")
        elif guess < self.secret_number:
            self.result_label.config(text="🔻 Too low! Try again.", fg="#007acc")
        elif guess > self.secret_number:
            self.result_label.config(text="🔺 Too high! Try again.", fg="#007acc")
        else:
            self.result_label.config(text="✅ Correct! You guessed it!", fg="#28a745")
            messagebox.showinfo("Congratulations!", "🎉 You guessed the number correctly!")

    def restart_game(self):
        self.secret_number = random.randint(1, 10)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        messagebox.showinfo("Game Restarted", "A new number has been chosen!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
