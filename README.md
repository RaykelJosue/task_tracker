# Task Tracker CLI

Task Tracker es una aplicación de línea de comandos (CLI) que permite gestionar tareas y listas de tareas. Puedes agregar, actualizar, eliminar, y marcar tareas como "en progreso" o "completadas". Las tareas se almacenan en un archivo JSON.

## Requisitos
```diff
- Python 3.x
- No requiere dependencias externas
```

## Instalación
```diff
1. Clona este repositorio o descarga los archivos del proyecto desde Git Bash o tu terminal de preferencia:
  git clone https://github.com/RaykelJosue/task_tracker.git

2. Crea un entorno virtual (opcional pero recomendado):
   python -m venv venv
   source venv/Scripts/activate
```

## Uso

Comandos disponibles:
```diff
1. Para agregar una nueva tarea:

python task-cli.py add "Descripción de la tarea"
Esto agregará una nueva tarea con el estado "todo".

2. Para listar una tarea:
python task-cli.py list
Esto lista todas las tareas. También puedes filtrarlas por estado usando los siguientes filtros:
todo (tareas pendientes)
in-progress (tareas en progreso)
done (tareas completadas)
Ejemplo : python task-cli.py list todo

3. Para actualizar una tarea:
python task-cli.py update <id> "Nueva descripción de la tarea"

4. Marcar una tarea como "en progreso" o "completada"
python task-cli.py mark <id> <estado>

5. Eliminar una tarea:
python task-cli.py delete <id>
```

# Ejemplos:
```diff
Agregar una tarea: python task-cli.py add "Comprar leche"
Actualizar una tarea: python task-cli.py update 1 "Comprar leche y pan"
Listar tareas en progreso: python task-cli.py list in-progress
Marcar una tarea como completada: python task-cli.py mark 1 done
Eliminar una tarea: python task-cli.py delete 1
```

Ejemplo de cómo quedaría el archivo tasks.json:
```diff
[
  {
    "id": 1,
    "description": "Comprar leche",
    "status": "todo",
    "createdAt": "2025-01-01T12:00:00",
    "updatedAt": "2025-01-01T12:00:00"
  }
]
```