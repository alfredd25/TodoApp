import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.file_path = "tasks.txt"

        self.tasks = self.load_tasks()

        self.setup_ui()

    def setup_ui(self):
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.edit_tasks = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_tasks.pack(pady=5)

        self.delete_tasks = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_tasks.pack(pady=5)

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
            return[]

    def save_task(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")