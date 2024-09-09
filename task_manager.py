import argparse # for # for parsing command arguments cli
from datetime import datetime 
import json # for storage

class Task:
    def __init__(self, task_id, description, status=None, createdAt=None, updatedAt=None, priority=None):
        self.id = task_id
        self.description = description
        self.status = status
        self.createdAt = datetime.fromisoformat(createdAt) if createdAt else datetime.now()
        self.updatedAt = datetime.fromisoformat(updatedAt) if updatedAt else datetime.now()
        self.priority = priority

    def display(self):
        data = [{
            'ID': self.id,
            'Description': self.description,
            'Status': self.status,
            'Created At': self.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
            'Updated At': self.updatedAt.strftime('%Y-%m-%d %H:%M:%S'),
            'Priority': self.priority
        }]
        return data

    def status_update(self, new_status):
        self.status = new_status
        self.updatedAt = datetime.now()

class TaskManager:
    def __init__(self, storage_file='tasks.json'):
        self.storage_file = storage_file
        self.task_dict = self.load_tasks()

    '''In load_tasks:
	The JSON file stores data in a dictionary-like format. When we load this data, 
	we convert it back into Python objects—specifically, 
	Task objects. This makes it easier to work with tasks in the program.'''

    def load_tasks(self):
        try:
            with open(self.storage_file, 'r') as f:
                file_content = f.read().strip()
                if not file_content:  # Check if the file is empty
                    return {}
                data = json.loads(file_content)
                return {task_id: Task(task_id=task_data.get('id'),
                                      description=task_data.get('description'),
                                      status=task_data.get('status'),
                                      createdAt=task_data.get('createdAt'),
                                      updatedAt=task_data.get('updatedAt'),
                                      priority=task_data.get('priority'))
                        for task_id, task_data in data.items()}
        except FileNotFoundError:
            return {}
        
    '''In save_tasks:
	When saving tasks to the JSON file, we need to convert these Task objects back into simple dictionaries. 
	JSON does not know how to handle custom Python objects like Task, so it needs to be in a serializable format (e.g., dictionaries, lists, strings, etc.). 
	Therefore, converting each Task object to a dictionary (task.__dict__) before saving is essential.'''

    def save_tasks(self):
        with open(self.storage_file, 'w') as f:
            data = {task_id: {
                'id': task.id,
                'description': task.description,
                'status': task.status,
                'createdAt': task.createdAt.isoformat(),
                'updatedAt': task.updatedAt.isoformat(),
                'priority': task.priority
            } for task_id, task in self.task_dict.items()}
            json.dump(data, f, indent=4)
            print(f"Tasks saved.")

    def add_task(self, task_id, description, status=None, priority=None):
        if task_id in self.task_dict:
            print(f"Task with ID {task_id} already exists.")
            return
        self.task_dict[task_id] = Task(task_id, description, status, priority=priority)
        print(f"Task added successfully (ID: {task_id})")
        self.save_tasks()

    def update_task(self, task_id, new_description=None, new_status=None, new_priority=None):
        if task_id in self.task_dict:
            task = self.task_dict[task_id]
            if new_description:
                task.description = new_description
            if new_status:
                task.status_update(new_status)
            if new_priority:
                task.priority = new_priority
            print(f"Task updated successfully (ID: {task_id})")
            self.save_tasks()
        else:
            print(f"Task not found (ID: {task_id})")

    def delete_task(self, task_id):
        if task_id in self.task_dict:
            del self.task_dict[task_id]
            self.save_tasks()  # Save changes after deletion
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task not found (ID: {task_id})")

    def list_tasks(self):
        if not self.task_dict:
            print("No tasks to display.")
            return
        print("Listing all tasks:")
        for task_id, task in self.task_dict.items():
            data = task.display()
            for entry in data:
                print(entry)



    def list_tasks_in_progress(self):
        done_tasks = {task_id: task for task_id, task in self.task_dict.items() if task.status == "in-progress"}
        
        if not done_tasks:
            print("No tasks with 'Done' status to display.")
            return
        
        print("Listing all tasks with 'Done' status:")
        for task_id, task in done_tasks.items():
            data = task.display()
            for entry in data:
                print(entry)

    def list_tasks_done(self):
        done_tasks = {task_id: task for task_id, task in self.task_dict.items() if task.status == "Done"}
        
        if not done_tasks:
            print("No tasks with 'Done' status to display.")
            return
        
        print("Listing all tasks with 'Done' status:")
        for task_id, task in done_tasks.items():
            data = task.display()
            for entry in data:
                print(entry)


def main():
    manager = TaskManager()

    parser = argparse.ArgumentParser(prog='task-cli')
    parser.add_argument('command', choices=['add', 'update', 'delete', 'list', 'mark-in-progress', 'mark-done'])
    parser.add_argument('task_id', nargs='?', default=None) # nargs? means optional
    parser.add_argument('description', nargs='?', default=None)
    parser.add_argument('status', nargs='?', default=None)
    parser.add_argument('priority', nargs='?', default=None)
    args = parser.parse_args()

    if args.command == 'add':
        task_id = input("Enter Task ID: ")
        description = input("Enter Description: ")
        status = input("Enter Status (to-do/in-progress/Done/, default: 'Pending'): ") or 'Pending'
        priority = input("Enter Priority (default: 'Low'): ") or 'Low'
        manager.add_task(task_id, description, status, priority)

    elif args.command == 'update':
        task_id = input("Enter Task ID to update: ")
        new_description = input("Enter new Description: ")
        new_status = input("Enter new Status (to-do/in-progress/Done/): ")
        new_priority = input("Enter new Priority: ")
        manager.update_task(task_id, new_description, new_status, new_priority)

    elif args.command == 'delete':
        task_id = input("Enter Task ID to delete: ")
        manager.delete_task(task_id)

    elif args.command == 'list':
        manager.list_tasks()

    elif args.command == 'list_tasks_in_progress':
        manager.list_tasks_in_progress()

    elif args.command == 'list_tasks_done':
        manager.list_tasks_done()


    elif args.command == 'mark-in-progress':
        task_id = input("Enter Task ID to mark as In Progress: ")
        manager.update_task(task_id, new_status="In Progress")

    elif args.command == 'mark-done':
        task_id = input("Enter Task ID to mark as Done: ")
        manager.update_task(task_id, new_status="Done")

if __name__ == "__main__":
    main()
