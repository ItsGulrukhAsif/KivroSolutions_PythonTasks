# Task 3 - Simple To-Do List App

def add_task(task_list):
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"✔ Task '{task}' added successfully.\n")

def view_tasks(task_list):
    if not task_list:
        print("📭 No tasks found.\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
        print()

def delete_task(task_list):
    if not task_list:
        print("📭 No tasks available to delete.\n")
        return
    view_tasks(task_list)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(task_list):
            removed_task = task_list.pop(index - 1)
            print(f"🗑 Task '{removed_task}' deleted successfully.\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main():
    task_list = []
    while True:
        print("========== To-Do List App ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("====================================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            print("👋 Exiting... Goodbye! ")
            break
        else:
            print("❌ Invalid choice! Please select between 1-4.\n")

if __name__ == "__main__":
    main()
