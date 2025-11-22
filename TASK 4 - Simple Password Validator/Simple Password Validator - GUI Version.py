import customtkinter as ctk
from tkinter import messagebox

# ------------------- Window Setup ------------------- #
ctk.set_appearance_mode("dark")  # dark or light
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Validator")
app.geometry("420x360")
app.resizable(False, False)

# ------------------- Validation Function ------------------- #
def validate_password():
    password = password_entry.get()

    if len(password) < 6:
        messagebox.showerror("Invalid", "Password must be at least 6 characters long.")
        status_label.configure(text="❌ Invalid Password", text_color="red")
        return

    if not any(char.isdigit() for char in password):
        messagebox.showerror("Invalid", "Password must contain at least one number.")
        status_label.configure(text="❌ Invalid Password", text_color="red")
        return

    if not any(char.isupper() for char in password):
        messagebox.showerror("Invalid", "Password must contain at least one uppercase letter.")
        status_label.configure(text="❌ Invalid Password", text_color="red")
        return

    messagebox.showinfo("Success", "Password Accepted!")
    status_label.configure(text="✔ Password Accepted", text_color="green")


def reset():
    password_entry.delete(0, "end")
    status_label.configure(text="")

# ------------------- Widgets ------------------- #
title_label = ctk.CTkLabel(app, text="🔐 Password Validator", font=("Segoe UI", 22, "bold"))
title_label.pack(pady=15)

password_entry = ctk.CTkEntry(app, placeholder_text="Enter password...", font=("Segoe UI", 15), width=280, height=40, show="*")
password_entry.pack(pady=10)

validate_button = ctk.CTkButton(app, text="Validate", command=validate_password, width=150, height=40)
validate_button.pack(pady=8)

reset_button = ctk.CTkButton(app, text="Reset", fg_color="gray", hover_color="#555", command=reset, width=120, height=35)
reset_button.pack()

status_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 18, "bold"))
status_label.pack(pady=15)

# ------------------- Run App ------------------- #
app.mainloop()
