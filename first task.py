import json

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load existing tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    task = {
        'description': description,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{idx}. {task['description']} [{status}]")

# Update task completion status
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            save_tasks(tasks)
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task {task_number} deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

def add_task_gui():
    description = task_entry.get()
    if description:
        tasks.append({'description': description, 'completed': False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task description")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task['completed'] else "Not Completed"
        task_listbox.insert(tk.END, f"{task['description']} [{status}]")

def mark_completed():
    try:
        selected_task_idx = task_listbox.curselection()[0]
        tasks[selected_task_idx]['completed'] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed")

def delete_task_gui():
    try:
        selected_task_idx = task_listbox.curselection()[0]
        tasks.pop(selected_task_idx)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

# Set up Tkinter window
root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task_gui)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
delete_button.pack(pady=5)

# Initialize tasks and update the list
tasks = load_tasks()
update_task_list()

root.mainloop()
