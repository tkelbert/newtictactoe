import math
import json
from rich.progress import track
import time
from rich.console import Console
from rich.table import Table

# Define the number of steps
total_steps = 50

# Use the track function to create a progress bar
for step in track(range(total_steps), description="Processing..."):
    # Simulate some work
    time.sleep(0.01)


class Todolist:
    def __init__(self):
        self.tasks = []
        self.new_item = []

    def display_list(self):
        print("================")
        print("PRINTING THE TASK LIST")
        for i in range(len(self.tasks)):
            print(self.tasks[i])

    def display_formatted_list(self):
        print("\n ==== The Todo List ====")
        if not self.tasks:
            print("no hay nada")
        else:
            for index, task_item in enumerate(self.tasks, start=1):
                description = task_item['task']
                is_completed = task_item['completed']

                # create a status marker
                status_marker = "[X]" if is_completed else "[ ]"

                print(f"{index}. {status_marker}: {description}")
            print("===================================")

    def display_list_rich(self):
        console = Console()
        table = Table(title="Todo List")

        table.add_column("Task", justify="left", style="cyan")
        table.add_column("Status", justify="center", style="magenta")

        for task in self.tasks:
            status = "Completed" if task['completed'] else "incomplete"
            table.add_row(task['task'], status)

        console.print(table)

    def get_new_list_item(self):
        new_item = input("Please add a task to the todo list > ")
        if not new_item:
            print("Incorrect input, please try again")
            return False
        else:
            self.new_item = new_item

    '''def add_item(self, item_added=None):
        if item_added == None:
            item_added = self.new_item
        my_keys = ['task']
        my_values = [item_added]
        for keys, values in zip(my_keys, my_values):
            self.tasks['task'] = values
        self.display_list_rich()'''

    def add_item(self, task_description):
        # adds a new task item to the list.

        # args:
        # task_description(str)

        if not task_description or not isinstance(task_description, str):
            print('invalid task description provided')
            return

        new_task = {'task': task_description, 'completed': False}
        self.tasks.append(new_task)
        print(f"\n{new_task} added to the todolist")


todo_list = []
task = [{'task': 'Buy groceries', 'completed': False},
        {'task': 'do python project', 'completed': False},
        {'task': 'make concrete weights', 'completed': False},
        {'task': 'learn rich libaray', 'completed': False}]
todo = Todolist()
running = True
todo.tasks = task

# while running:

todo.display_list()
todo.display_formatted_list()
todo.display_list_rich()
todo.add_item('do a flip')
todo.display_list_rich()

'''while running:'''
table = Table(title="TODO list management")
