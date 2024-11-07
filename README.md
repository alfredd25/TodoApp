To-Do List Application
A simple, intuitive To-Do List application built with Python and Tkinter, allowing users to manage their tasks efficiently. This app supports adding, editing, deleting tasks, and marking tasks as complete, with persistent storage to keep tasks saved across sessions.

Features
Add, Edit, and Delete Tasks: Users can add new tasks, edit existing tasks, and delete completed or unwanted tasks.
Intuitive UI: User-friendly interface with clear section headings and a soft, pale color scheme.
Persistent Storage: Tasks are saved locally and loaded on app startup, so users can pick up where they left off.
Requirements
Python 3.x
Tkinter: Tkinter is included with standard Python installations, so no separate installation is needed.
To install the required library (if not already included in your Python installation):

bash
Copy code
pip install tk
Setup and Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/alfredd25/TodoApp.git
cd TodoApp
Run the Application:

bash
Copy code
python main.py
Using the App:

Add tasks by typing in the entry field and clicking Add Task.
Mark tasks as complete by clicking the checkboxes next to each task.
Tasks will persist when you close and reopen the app.
File Structure
main.py: The main file to start the application.
ToDo_app.py: Contains the main TodoApp class and all app functionality.
tasks.txt: Stores the tasks persistently across sessions.
Screenshots
![image](https://github.com/user-attachments/assets/57288717-584d-4bcb-b42e-2344492a1cba)


License
This project is open-source and available for modification and distribution.
