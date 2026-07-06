# CRUD BASICO CON FASTAPI Y SQLALCHEMY, USANDO POO PARA DEFINIR CLASES 
#FUTURAMENTE CADA CLASE ESTRARA EN SU PROPIO ARCHIVO

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Inicializamos FastAPI
app = FastAPI()

# Configuración de la base de datos SQLite con SQLAlchemy 
# #aqui nos conectamos a la base de datos la cual estara en un archivo llamado trackit.db
engine = create_engine("sqlite:///trackit.db", echo=True, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Clase Item usando POO + SQLAlchemy para que cada objeto tenga nombre y ubicacion en la base de datos
#recuerda que cada tabla en la base de datos sera una clase y cada columna un atributo de la clase 
#asi como cada fila un objeto de la clase o una instancia de la clase (es lo mismo (objeto=instancia)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, default="desconocida")

# Creamos la tabla en la base de datos para la clase Item
Base.metadata.create_all(bind=engine)

# Función para obtener sesión
#Yo se q no sabes quizas que es el uso de excepciones pero es para manejar errores en el codigo
#aqui se usa para asegurar que la sesion se cierre correctamente despues de usarla
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# =================== CRUD ===================

# Crear objeto en la tabla de items y asi pues se agregara un nuevo item a la base de datos osea una nueva fila
@app.post("/item/")
def create_item(name: str, location: str = "desconocida"):
    session = next(get_session())
    item = Item(name=name, location=location)
    session.add(item)
    session.commit()
    session.refresh(item)
    return {"id": item.id, "name": item.name, "location": item.location}

# Leer todos los objetos esto en la tabla seria un SELECT * FROM items
#ese comando SQL significa seleccionar todos los items de la tabla items
@app.get("/items/")
def read_items():
    session = next(get_session())
    items = session.query(Item).all()
    return [{"id": i.id, "name": i.name, "location": i.location} for i in items]

# Leer un objeto por ID  esto seria un SELECT * FROM items WHERE id=item_id
#ese comando SQL significa seleccionar el item con el id especificado
@app.get("/item/{item_id}")
def read_item(item_id: int):
    session = next(get_session())
    item = session.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"id": item.id, "name": item.name, "location": item.location}

# Actualizar un objeto esto seria un UPDATE items SET name=new_name, location=new_location WHERE id=item_id
#esos comandos SQL significan actualizar el nombre y la ubicacion del item con el id especificado
@app.put("/item/{item_id}")
def update_item(item_id: int, name: str = None, location: str = None):
    session = next(get_session())
    item = session.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    if name:
        item.name = name
    if location:
        item.location = location
    session.commit()
    return {"id": item.id, "name": item.name, "location": item.location}

# Borrar un objeto seria un DELETE FROM items WHERE id=item_id
#ese comando SQL significa borrar el item con el id especificado
@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    session = next(get_session())
    item = session.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    session.delete(item)
    session.commit()
    return {"mensaje": f"Item {item_id} eliminado"}