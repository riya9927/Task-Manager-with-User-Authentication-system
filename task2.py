import hashlib
import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.users_file = "users.json"
        self.tasks_file = "tasks.json"
        self.current_user = None
        self.load_data()

    def load_data(self):
        # Initialize or load users data
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}
            self.save_users()

        # Initialize or load tasks data
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = {}
            self.save_tasks()

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    def save_tasks(self):
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.users:
            return False, "Username already exists!"
        
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        self.tasks[username] = []  # Initialize empty task list for new user
        self.save_users()
        self.save_tasks()
        return True, "Registration successful!"

    def login(self, username, password):
        if username not in self.users:
            return False, "Username not found!"
        
        if self.users[username] == self.hash_password(password):
            self.current_user = username
            return True, "Login successful!"
        return False, "Incorrect password!"

    def add_task(self, description):
        if not self.current_user:
            return False, "Please login first!"
        
        task = {
            "id": len(self.tasks[self.current_user]) + 1,
            "description": description,
            "status": "Pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks[self.current_user].append(task)
        self.save_tasks()
        return True, "Task added successfully!"

    def view_tasks(self):
        if not self.current_user:
            return False, "Please login first!"
        
        if not self.tasks[self.current_user]:
            return True, "No tasks found!"
        
        tasks_list = []
        for task in self.tasks[self.current_user]:
            tasks_list.append(
                f"ID: {task['id']}, Description: {task['description']}, "
                f"Status: {task['status']}, Created: {task['created_at']}"
            )
        return True, "\n".join(tasks_list)

    def mark_completed(self, task_id):
        if not self.current_user:
            return False, "Please login first!"
        
        for task in self.tasks[self.current_user]:
            if task['id'] == task_id:
                task['status'] = "Completed"
                self.save_tasks()
                return True, "Task marked as completed!"
        return False, "Task not found!"

    def delete_task(self, task_id):
        if not self.current_user:
            return False, "Please login first!"
        
        for i, task in enumerate(self.tasks[self.current_user]):
            if task['id'] == task_id:
                self.tasks[self.current_user].pop(i)
                self.save_tasks()
                return True, "Task deleted successfully!"
        return False, "Task not found!"

    def logout(self):
        if not self.current_user:
            return False, "No user is currently logged in!"
        
        self.current_user = None
        return True, "Logged out successfully!"

def main():
    task_manager = TaskManager()
    
    while True:
        if not task_manager.current_user:
            print("\n=== Task Manager ===")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                success, message = task_manager.register(username, password)
                print(message)
            
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                success, message = task_manager.login(username, password)
                print(message)
            
            elif choice == "3":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice!")
        
        else:
            print(f"\n=== Welcome {task_manager.current_user} ===")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Logout")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                description = input("Enter task description: ")
                success, message = task_manager.add_task(description)
                print(message)
            
            elif choice == "2":
                success, message = task_manager.view_tasks()
                print(message)
            
            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                success, message = task_manager.mark_completed(task_id)
                print(message)
            
            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                success, message = task_manager.delete_task(task_id)
                print(message)
            
            elif choice == "5":
                success, message = task_manager.logout()
                print(message)
            
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main()