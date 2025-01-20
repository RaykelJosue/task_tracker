import argparse
import json
import os
from datetime import datetime

# Ruta del archivo JSON que guardará las tareas
TASKS_FILE = 'tasks.json'

# Asegurarse de que el archivo JSON exista
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)

# Función para cargar las tareas desde el archivo JSON
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: El archivo de tareas no existe. Creando uno nuevo.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo de tareas está corrupto.")
        return []
    except Exception as e:
        print(f"Error al cargar las tareas: {e}")
        return []

# Función para guardar las tareas en el archivo JSON
def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error al guardar las tareas: {e}")

# Función para agregar una nueva tarea
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')

# Función para listar todas las tareas
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        # Validación para asegurarse de que el estado sea uno de los valores válidos
        if status not in ['todo', 'in-progress', 'done']:
            print(f"Error: '{status}' no es un estado válido. Usa 'todo', 'in-progress' o 'done'.")
            return
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")


# Función para actualizar una tarea
def update_task(task_id, new_description):
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['description'] = new_description
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f'Task ID {task_id} updated successfully.')
    else:
        print(f'Task with ID {task_id} not found.')

# Función para marcar una tarea como 'in-progress' o 'done'
def mark_task(task_id, status):
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['status'] = status
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f'Task ID {task_id} marked as {status}.')
    else:
        print(f'Task with ID {task_id} not found.')

# Función para eliminar una tarea
def delete_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        tasks = [t for t in tasks if t['id'] != task_id]
        save_tasks(tasks)
        print(f'Task ID {task_id} deleted successfully.')
    else:
        print(f"Error: Task with ID {task_id} not found.")

# Función de validación de ID
def valid_task_id(value):
    try:
        id_value = int(value)  # Intentamos convertir el valor a entero
        if id_value < 1:  # Verificamos que el ID sea un número positivo
            raise argparse.ArgumentTypeError("ID must be a positive integer.")  # Lanzamos un error si no es positivo
        return id_value  # Si es válido, retornamos el valor convertido a entero
    except ValueError:
        raise argparse.ArgumentTypeError("ID must be a positive integer.")  # Lanzamos un error si no se puede convertir a entero

# Configuración de la CLI
def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')

    # Subcomandos para agregar, listar, actualizar, etc.
    subparsers = parser.add_subparsers(dest='command')

    # Subcomando para agregar tareas
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Description of the task')

    # Subcomando para listar tareas
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.add_argument('status', choices=['todo', 'in-progress', 'done'], nargs='?', help='Filter by task status')

    # Subcomando para actualizar tareas
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=valid_task_id, help='ID of the task to update')
    update_parser.add_argument('description', help='New description of the task')

    # Subcomando para marcar tareas
    mark_parser = subparsers.add_parser('mark', help='Mark a task as in progress or done')
    mark_parser.add_argument('id', type=valid_task_id, help='ID of the task')
    mark_parser.add_argument('status', choices=['in-progress', 'done'], help='New status of the task')

    # Subcomando para eliminar tareas
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=valid_task_id, help='ID of the task to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks(args.status)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'mark':
        mark_task(args.id, args.status)
    elif args.command == 'delete':
        delete_task(args.id)

if __name__ == '__main__':
    main()
