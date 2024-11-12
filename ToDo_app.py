import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        self.light_theme = {
            "bg": "#faf3e0",
            "fg": "#000000",
            "button_bg": "#e6d5b2",
            "entry_bg": "#ffffff",
            "task_bg": "#ffffff",
            "label_bg": "#faf3e0"
        }

        self.dark_theme = {
            "bg": "#2e2e2e",
            "fg": "#ffffff",
            "button_bg": "#555555",
            "entry_bg": "#3e3e3e",
            "task_bg": "#4e4e4e",
            "label_bg": "#2e2e2e"
        }

        self.image = Image.open("dark_mode.png")
        self.image = self.image.resize((30, 30))
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.current_theme = self.dark_theme

        self.file_path = "tasks.txt"
        self.tasks = self.load_tasks()

        self.setup_ui()
        self.toggle_theme()
        self.update_task_list()

    def setup_ui(self):
        self.add_task_label = tk.Label(self.root, text="Add Task", font=("Arial", 14, "bold"))
        self.add_task_label.pack(pady=(10, 0))

        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_list_label = tk.Label(self.root, text="Task List", font=("Arial", 14, "bold"))
        self.task_list_label.pack(pady=(20, 0))

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.edit_task_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack(pady=5)

        self.delete_tasks = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_tasks.pack(pady=5)

        self.complete_task_button = tk.Button(self.root, text="Mark Complete", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.toggle_button = tk.Button(self.root, image=self.image_tk, command=self.toggle_theme)
        self.toggle_button.place(relx=1.0, rely=0.0, x=-10, y=10, anchor='ne')

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def edit_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[index]

            task_text = selected_task["text"] if isinstance(selected_task, dict) else selected_task
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task_text)

            self.delete_task()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit")


    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.update_task_list()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = "✓ " + task["text"] if task["completed"] else task["text"]
            self.task_listbox.insert(tk.END, display_text)

    def load_tasks(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                tasks = [self.parse_task(line.strip()) for line in file.readlines()]
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(self.format_task(task) + "\n")

    def parse_task(self, line):
        if line.startswith("✓ "):
            return {"text": line[2:], "completed": True}
        return {"text": line, "completed": False}

    def format_task(self, task):
        return "✓ " + task["text"] if task["completed"] else task["text"]

    def toggle_theme(self):
        self.current_theme = self.dark_theme if self.current_theme == self.light_theme else self.light_theme
        self.root.configure(bg=self.current_theme["bg"])
        self.task_entry.config(bg=self.current_theme["entry_bg"], fg=self.current_theme["fg"])
        self.add_task_button.config(bg=self.current_theme["button_bg"], fg=self.current_theme["fg"])
        self.complete_task_button.config(bg=self.current_theme["button_bg"], fg=self.current_theme["fg"])
        self.edit_task_button.config(bg=self.current_theme["button_bg"], fg=self.current_theme["fg"])
        self.delete_tasks.config(bg=self.current_theme["button_bg"], fg=self.current_theme["fg"])
        self.toggle_button.config(bg=self.current_theme["button_bg"], fg=self.current_theme["fg"])
        self.task_listbox.config(bg=self.current_theme["task_bg"], fg=self.current_theme["fg"])
        self.add_task_label.config(bg=self.current_theme["label_bg"], fg=self.current_theme["fg"])
        self.task_list_label.config(bg=self.current_theme["label_bg"], fg=self.current_theme["fg"])
