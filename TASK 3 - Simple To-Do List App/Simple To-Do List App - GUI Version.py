import customtkinter as ctk
from tkinter import messagebox
import os

# ------------------- Window Setup ------------------- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern To-Do List App")
app.geometry("420x580")
app.resizable(False, False)

# List that stores tasks in format: [(task_text, completed_bool)]
tasks = []

# ------------------- File Handling ------------------- #
FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                text, status = line.strip().rsplit("|", 1)
                tasks.append([text, status == "True"])
        update_task_list()

def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task_text, completed in tasks:
            file.write(f"{task_text}|{completed}\n")

# ------------------- Functions ------------------- #
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append([task, False])
        task_entry.delete(0, "end")
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task_list():
    for widget in task_listbox.winfo_children():
        widget.destroy()

    for index, (task_text, completed) in enumerate(tasks):
        checkbox = ctk.CTkCheckBox(
            task_listbox,
            text=f"{index+1}. {task_text}",
            font=("Segoe UI", 14, "bold"),
            command=lambda i=index: toggle_complete(i)
        )
        checkbox.pack(anchor="w", pady=3)

        if completed:
            checkbox.select()
            checkbox.configure(text_color="gray")
        else:
            checkbox.deselect()
            checkbox.configure(text_color="white")

def toggle_complete(index):
    tasks[index][1] = not tasks[index][1]
    save_tasks()
    update_task_list()

def delete_task():
    selected_num = delete_entry.get().strip()
    
    if not selected_num.isdigit():
        messagebox.showerror("Error", "Enter task number only.")
        return
    
    selected_num = int(selected_num)
    
    if 1 <= selected_num <= len(tasks):
        tasks.pop(selected_num - 1)
        delete_entry.delete(0, "end")
        update_task_list()
        save_tasks()
    else:
        messagebox.showerror("Error", "Invalid task number.")

def clear_all():
    if tasks:
        confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
        if confirm:
            tasks.clear()
            update_task_list()
            save_tasks()
    else:
        messagebox.showinfo("Info", "No tasks to clear.")

# ------------------- Widgets ------------------- #
title_label = ctk.CTkLabel(app, text="📋 To-Do List Manager", font=("Segoe UI", 24, "bold"))
title_label.pack(pady=12)

task_entry = ctk.CTkEntry(app, placeholder_text="Enter new task...", font=("Segoe UI", 15), width=300, height=40)
task_entry.pack(pady=10)

add_button = ctk.CTkButton(app, text="Add Task", font=("Segoe UI", 15), command=add_task, width=170, height=40)
add_button.pack(pady=5)

task_listbox = ctk.CTkScrollableFrame(app, width=360, height=260)
task_listbox.pack(pady=10)

delete_entry = ctk.CTkEntry(app, placeholder_text="Task number to delete...", font=("Segoe UI", 14), width=200, height=35)
delete_entry.pack(pady=5)

delete_button = ctk.CTkButton(app, text="Delete Task", command=delete_task, width=160, height=38)
delete_button.pack(pady=3)

clear_button = ctk.CTkButton(app, text="Clear All", fg_color="red", hover_color="#a30000",
                             command=clear_all, width=160, height=38)
clear_button.pack(pady=7)

# ------------------- Load Saved Tasks ------------------- #
load_tasks()

# ------------------- Start App ------------------- #
app.mainloop()
