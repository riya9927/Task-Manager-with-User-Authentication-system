# Task Manager with User Authentication

## Project Description
This **Task Manager** is a Python-based application designed to help users manage their tasks in a structured and secure way. It includes a robust **user authentication system**, allowing users to create, view, update, and delete their tasks while ensuring data security and user-specific task storage.

## Features
- **User Registration and Login**:
  - Secure password hashing.
  - Unique username validation.

- **Task Management**:
  - Add, view, mark as completed, and delete tasks.
  - Task ID assignment and status tracking (Pending/Completed).
  - Persistent task storage for each user.

- **Interactive Menu**:
  - User-friendly interface for task operations and logout functionality.

## Prerequisites
- **Python** (Version >= 3.6)
- Basic understanding of Python programming.

## How It Works
1. **User Authentication**:
   - New users register with a unique username and password.
   - Registered users log in with their credentials to access the Task Manager.

2. **Task Operations**:
   - **Add Task**: Input a description to create a new task.
   - **View Tasks**: Display all tasks with their details (ID, description, status, creation date).
   - **Mark Task as Completed**: Update the task status.
   - **Delete Task**: Remove a task by its ID.

3. **Data Management**:
   - User credentials are stored in `users.json` with hashed passwords.
   - Tasks are stored in `tasks.json` for each user.

4. **Menu-Driven Interface**:
   - Easy navigation between task operations and logout.

## File Structure
- `users.json`: Stores user credentials.
- `tasks.json`: Stores user-specific tasks.
- `task_manager.py`: Main application file containing the Task Manager implementation.

