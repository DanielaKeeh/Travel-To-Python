# 🐍 Travel To Python — Mi portafolio de aprendizaje

¡Holis! Soy Dan 👋. Este repo es mi bitácora de aprendizaje de Python: empecé desde cero y aquí voy documentando cada proyecto, ejercicio y cosa nueva que aprendo. Va creciendo poco a poco, así que si vuelves a pasar seguro hay algo nuevo.

## 🚀 Características principales

- **4 proyectos** organizados de forma modular, del más básico al más avanzado
- **Sistema de menús interactivos** anidados para navegar los ejercicios
- **Progresión clara**: de fundamentos → ejercicios prácticos → proyecto integrador → API con base de datos
- **Último proyecto: Trackit**, un CRUD con **FastAPI + SQLAlchemy**
- Código comentado en español, explicando el "por qué" y no solo el "qué"

## 📂 Estructura del proyecto

| Carpeta | Descripción | Archivos principales |
|---------|-------------|----------------------|
| 📁 [`Introduccion/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/Introduccion) | 🐣 Fundamentos de Python | `AprendiendoPython.py`, `EjerciciosBasicos.py`, `EjerciciosCondicionales.py` |
| 📁 [`PrimerProyecto/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/PrimerProyecto) | 🔧 Ejercicios prácticos / validadores | `ValidarContrasena.py`, `ClasificarEdad.py`, `VerificadorVotacion.py`, `numeros.py` |
| 📁 [`SegundoProyecto/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/SegundoProyecto) | 🧁 Proyecto integrador: Kokomi Bakery | `DataBase.py`, `Pedidos.py` |
| 📁 [`CRUD-python/`](https://github.com/DanielaKeeh/Travel-To-Python/tree/main/CRUD-python) | 🗃️ Trackit: CRUD con FastAPI + SQLAlchemy | `main.py`, `trackit.db` |
| 📄 [`main.py`](https://github.com/DanielaKeeh/Travel-To-Python/blob/main/main.py) | Menú principal del repo | — |

## 📝 Descripción de cada proyecto

### `Introduccion/`
Conceptos básicos de Python: variables, tipos de datos, operadores, condicionales y bucles.

### `PrimerProyecto/`
Ejercicios prácticos enfocados en validaciones: contraseñas, clasificación por edad, verificación de requisitos para votar, y trabajo con números.

### `SegundoProyecto/` — Kokomi Bakery 🧁
Mi primer proyecto integrador: un sistema de pedidos para una panadería, usando diccionarios como estructura de datos para productos, validación de stock y cálculo de precios.

### `CRUD-python/` — Trackit 🗃️
El proyecto más reciente y el salto más grande hasta ahora: una API con **FastAPI** para llevar registro de dónde dejaste tus pertenencias. Usa **SQLAlchemy** con Programación Orientada a Objetos para definir el modelo de datos y persistirlo en una base de datos **SQLite** (`trackit.db`). Implementa las 4 operaciones CRUD completas:

- `POST /item/` — crear un objeto
- `GET /items/` — listar todos los objetos
- `GET /item/{item_id}` — obtener un objeto por ID
- `PUT /item/{item_id}` — actualizar un objeto
- `DELETE /item/{item_id}` — eliminar un objeto

## 🛠️ Habilidades demostradas

### Fundamentos de Python
- Sintaxis básica: variables, tipos de datos, operadores
- E/S básica: `input()`, `print()`, f-strings
- Conversión de tipos: `int()`, `float()`, `str()`
- Operadores aritméticos, compuestos y de comparación

### Control de flujo
- Condicionales: `if`, `elif`, `else`
- Bucles: `while`, control con banderas booleanas
- Lógica booleana: `and`, `or`, condiciones compuestas

### Estructuras y organización
- Funciones: definición, parámetros, retorno de valores
- Módulos: importación y organización por carpetas
- Menús interactivos: sistemas anidados de navegación

### Kokomi Bakery
- Diccionarios como estructura de datos para productos
- Validaciones de stock y existencia de productos
- Cálculo de precios y cantidades disponibles
- Persistencia básica en memoria

### Trackit (CRUD API)
- **FastAPI** para exponer endpoints REST
- **SQLAlchemy** (ORM) + Programación Orientada a Objetos para modelar datos
- Persistencia real en base de datos **SQLite**
- Manejo de sesiones y manejo de errores con `HTTPException`
- CRUD completo: crear, leer, actualizar y eliminar

## ▶️ Cómo ejecutar

### Menú principal (Introducción, Primer y Segundo Proyecto)
```bash
python main.py
```
Requiere **Python 3.8+**.

### Trackit (CRUD con FastAPI)
```bash
cd CRUD-python
pip install fastapi sqlalchemy uvicorn
uvicorn main:app --reload
```
Luego abre `http://127.0.0.1:8000/docs` para probar los endpoints desde la documentación interactiva de FastAPI.

## 📌 Notas

Este repo lo sigo actualizando conforme voy aprendiendo cosas nuevas, con la meta de ir armando algo cada vez más grande y sólido.

## 🔜 Próximas actualizaciones

1. Uso de excepciones `try/except`
2. Programación Orientada a Objetos (POO)
3. Pandas y NumPy
4. Diccionarios más grandes y anidados
5. Problemas de Codeforces resueltos con explicación en comentarios
6. Más proyectos modularizados y escalables

---

Quizás no es mucho, pero está humilde jaja xddd

**— Dan :D**
