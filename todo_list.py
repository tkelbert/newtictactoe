import math
import json
from rich.progress import track
import time
from rich.console import Console
from rich.table import Table

# Define the number of steps
total_steps = 100
console = Console()
'''# Use the track function to create a progress bar
for step in track(range(total_steps), description="Processing..."):
    # Simulate some work
    time.sleep(0.01)
'''

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


    def display_list_rich_options(self):
        console = Console()
        table = Table(title="Todo List")
        table.add_column("Numbers", justify="left")

        table.add_column("Task", justify="left", style="cyan")
        table.add_column("Status", justify="center", style="magenta")
        i = 0 
        for task in self.tasks:
            i+=1
            status = "Completed" if task['completed'] else "incomplete"
            i = str(i)
            table.add_row(i, task['task'], status)
            i = int(i)
        console.print(table)
        
    def get_new_list_item(self):
        new_item = input("Please add a task to the todo list > ")
        if not new_item:
            print("Incorrect input, please try again")
            return False
        else:
            self.new_item = new_item
        return new_item

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

    def show_options(self):
        table = Table(title="TODO list management")
        table.add_column("NUMBER", style= "dim", justify="center")
        table.add_column("OPTIONS", style="magenta")
        table.add_row("1.","[green]Display the list[/green]")
        table.add_row("2.","[cyan]Add a new item to the list[/cyan]")
        table.add_row("3.", "[blue]Mark a task as completed[/blue] :white_check_mark:")
        table.add_row("4.","[red]Delete item from list permamently[/red]")
        table.add_row("5.","[orange]Save the todo list to a json file[/orange]:computer:")
        table.add_row("6.", "[bold red]Start a new dictionary[/bold red]")
        console.print(table)

    def mark_as_completed(self):

        task_marked = input("which task would you like to mark completed? > ")
        task_marked =int(task_marked) - 1
        a = len(self.tasks)
        print(f"a: {a}")
        if task_marked > a:
            print("that was not an option")
            return True
        self.tasks[task_marked]['completed'] = True

    def get_response(self):
        print("Which option do you want to do?")
        response = input("Enter the number of the option you'd like to do or q to quit: ")
        runner = True
        while runner == True:
            if response == 'q' or response == 'Q':
                print("quitting.....")
                runner = False
                return False
            try:
                response = int(response)
                runner = False
            except ValueError:
                print("You must enter an integer that corresponds to a number on the list of options.")
                response = input("Enter an integer >> ")
            except response == 'q' or 'Q':
                pass
            if response == 1:
                for step in track(range(total_steps), description="Loading to do list..."):
                # Simulate some work
                    time.sleep(0.01)

                self.display_list_rich()
                return True
            if response == 2:
                task_description = self.get_new_list_item()
                for step in track(range(total_steps), description= "Adding new item...."):
                    time.sleep(0.01)
            
                self.add_item(task_description)
                todo.display_list_rich()
                return True
            if response == 3:
                self.display_list_rich_options()
                self.mark_as_completed()
                self.display_list_rich()
                return True
           
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
checker = True
while checker == True:
    todo.show_options()
    checker = todo.get_response()
