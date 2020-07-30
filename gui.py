import tkinter as tk
import database

class Todo(tk.Tk):
    def __init__(self, connection, current_user, tasks=None):
        super().__init__()

        self.connection = connection
        self.current_user = current_user

        if not tasks:
            self.tasks = []
        else:
            self.tasks = []
            for task in tasks:
                self.tasks.append(tk.Label(self, text=task, pady=10))

        self.title("To-Do App v1")
        self.geometry("300x400")

        todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg="white", fg="black")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.bind("<Return>", self.add_task)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)

            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)
            database.push_task(self.connection, self.current_user, new_task.cget('text'))

        self.task_create.delete(1.0, tk.END)

def display(connection, current_user, tasks):
    
    try:
        tasks = tasks.split(",")
    except:
        pass
    todo = Todo(connection, current_user, tasks)
    todo.mainloop()