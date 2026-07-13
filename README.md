# 🐍 Travel To Python — My Learning Portfolio

Hi! I'm Dan 👋. This repo is my Python learning log: I started from zero and I'm documenting every project, exercise, and new thing I learn along the way. It keeps growing little by little, so if you come back later there's probably something new.

## 🚀 Key Features

- **4 projects**, organized in a modular way, from the most basic to the most advanced
- **Nested interactive menu system** to navigate the exercises
- **Clear progression**: fundamentals → practical exercises → integrative project → API with a database
- **Latest project: Trackit**, a CRUD built with **FastAPI + SQLAlchemy**
- Code commented in Spanish, explaining the "why" and not just the "what"

## 📂 Project Structure

| Folder | Description | Main files |
|---------|-------------|----------------------|
| 📁 [`Introduccion/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/Introduccion) | 🐣 Python fundamentals | `AprendiendoPython.py`, `EjerciciosBasicos.py`, `EjerciciosCondicionales.py` |
| 📁 [`PrimerProyecto/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/PrimerProyecto) | 🔧 Practical exercises / validators | `ValidarContrasena.py`, `ClasificarEdad.py`, `VerificadorVotacion.py`, `numeros.py` |
| 📁 [`SegundoProyecto/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/SegundoProyecto) | 🧁 Integrative project: Kokomi Bakery | `DataBase.py`, `Pedidos.py` |
| 📁 [`CRUD-python/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/CRUD-python) | 🗃️ Trackit: CRUD with FastAPI + SQLAlchemy | `main.py`, `trackit.db` |
| 📄 [`main.py`](https://github.com/DanielaKeeh/Travel-To-Python/blob/main/main.py) | Repo's main menu | — |

## 📝 Project descriptions

### `Introduccion/`
Basic Python concepts: variables, data types, operators, conditionals, and loops.

### `PrimerProyecto/`
Practical exercises focused on validation: passwords, age classification, voting eligibility checks, and number handling.

### `SegundoProyecto/` — Kokomi Bakery 🧁
My first integrative project: an order system for a bakery, using dictionaries as the data structure for products, stock validation, and price calculation.

### `CRUD-python/` — Trackit 🗃️
The most recent project and the biggest step up so far: an API built with **FastAPI** to keep track of where you left your belongings. It uses **SQLAlchemy** with Object-Oriented Programming to define the data model and persist it in an **SQLite** database (`trackit.db`). It implements all 4 CRUD operations:

- `POST /item/` — create an item
- `GET /items/` — list all items
- `GET /item/{item_id}` — get an item by ID
- `PUT /item/{item_id}` — update an item
- `DELETE /item/{item_id}` — delete an item

## 🛠️ Skills demonstrated

### Python fundamentals
- Basic syntax: variables, data types, operators
- Basic I/O: `input()`, `print()`, f-strings
- Type conversion: `int()`, `float()`, `str()`
- Arithmetic, compound, and comparison operators

### Control flow
- Conditionals: `if`, `elif`, `else`
- Loops: `while`, control with boolean flags
- Boolean logic: `and`, `or`, compound conditions

### Structure and organization
- Functions: definition, parameters, return values
- Modules: importing and organizing by folder
- Interactive menus: nested navigation systems

### Kokomi Bakery
- Dictionaries as the data structure for products
- Stock and product-existence validation
- Price and available-quantity calculations
- Basic in-memory persistence

### Trackit (CRUD API)
- **FastAPI** for exposing REST endpoints
- **SQLAlchemy** (ORM) + Object-Oriented Programming to model data
- Real persistence in an **SQLite** database
- Session handling and error handling with `HTTPException`
- Full CRUD: create, read, update, and delete

## ▶️ How to run

### Main menu (Intro, First and Second Project)
```bash
python main.py
```
Requires **Python 3.8+**.

### Trackit (CRUD with FastAPI)
```bash
cd CRUD-python
pip install fastapi sqlalchemy uvicorn
uvicorn main:app --reload
```
Then open `http://127.0.0.1:8000/docs` to test the endpoints from FastAPI's interactive documentation.

## 📌 Notes

I keep updating this repo as I learn new things, with the goal of building something bigger and more solid over time.

## 🔜 Upcoming updates

1. Using `try/except` exceptions
2. Object-Oriented Programming (OOP)
3. Pandas and NumPy
4. Larger, nested dictionaries
5. Codeforces problems solved with explanations in comments
6. More modular, scalable projects

---

Maybe it's not much, but it's humble hehe xddd

**— Dan :D**
