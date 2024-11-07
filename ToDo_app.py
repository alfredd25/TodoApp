import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        self.file_path = "tasks.txt"

        self.tasks = self.load_tasks()

        self.setup_ui()

        self.update_task_list()

    def setup_ui(self):
        self.root.configure(bg="#f5f5dc")

        add_task_label = tk.Label(self.root, text="Add Task", font=("Arial", 14, "bold"), bg="#f5f5dc")
        add_task_label.pack(pady=(10, 0))

        self.task_entry = tk.Entry(self.root, width=30, bg="#f0f0e4")
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#EADDCA", fg="#000000")
        self.add_task_button.pack(pady=5)

        task_list_label = tk.Label(self.root, text="Task List", font=("Arial", 14, "bold"), bg="#f5f5dc")
        task_list_label.pack(pady=(20, 0))

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, bg="#f0f0e4")
        self.task_listbox.pack(pady=10)

        self.edit_tasks = tk.Button(self.root, text="Edit Task", command=self.edit_task,bg="#EADDCA", fg="#000000")
        self.edit_tasks.pack(pady=5)

        self.delete_tasks = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="#EADDCA", fg="#000000")
        self.delete_tasks.pack(pady=5)

        self.task_frame = tk.Frame(self.root, bg="#f5f5dc")
        self.task_frame.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_task()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, selected_task)
            self.delete_task()
            self.save_task()

        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.update_task_list()
            self.save_task()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                tasks =[line.strip() for line in file.readlines()]
            return tasks

        except FileNotFoundError:
            return []

    def save_task(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
