class TaskManager:
    tasks = []
    global_task_id = 0

    def main(self):
        print("Aucune tâche pour le moment")

        command = ""
        while command != "exit":
            command = input()
            action = self.parse(command)
            self.parse_logic(action)

    def parse(self, command):
        word = ""

        if command[0] == "+":
            word = "add"
        elif command[0] == "-":
            word = "delete"
        elif command[0] == "x":
            word = "done"
        elif command == "0":
            word = "todo"

        description = command[2:]
        action = Action(word, description)
        return action

    def parse_logic(self, action):
        if action[0] == "add":
            self.tasks.append(action)
        elif action[0] == "delete":
            self.delete_task(action)
        elif action[0] == "done":
            self.tasks.append(action)
        elif action == "todo":
            self.tasks.append(action)

    def add_task(self, task):
        self.tasks.append(task)
        self.global_task_id += 1

    def delete_task(self, task):
        i = 0
        for _task in self.tasks:
            if _task.id == task.id:
                del self.tasks[i]


class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Task:
    def __init__(self, id, description):
        self.description = description
        self.id = id
        self.status = "à faire"

    def done(self):
        self.status = "fait"

    def todo(self):
        self.status = "à faire"
