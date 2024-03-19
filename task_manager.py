import json
from nlp_utils import predict_category
from datetime import date
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

class TaskManager:
    def __init__(self, data_file="data/tasks.json"):
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                tasks = json.load(f)
                for task in tasks:
                    task["due_date"] = datetime.fromisoformat(task["due_date"]).date()
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2, cls=CustomEncoder)

    def create_task(self, title, description, due_date):
        category = predict_category(title, description)
        task = {
            "title": title,
            "description": description,
            "category": category,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, title, description, due_date):
        task = self.tasks[index]
        task["title"] = title
        task["description"] = description
        task["due_date"] = due_date
        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def complete_task(self, index):
        self.tasks[index]["completed"] = True
        self.save_tasks()
        
    def save_tasks(self):
        with open(self.data_file, "w") as f:
            json.dump(self.tasks, f, indent=2, cls=CustomEncoder)