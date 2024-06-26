from fastapi import FastAPI
from pydantic import BaseModel

class Entity(BaseModel):
    id: int
    value: str | None = None

class Entity2:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

app = FastAPI()

@app.get('/')
def index():
    return {"Hello FastAPI!"}

@app.post("/entity/add")
def create_entity():
    entity = 'new entity'
    return {"entity": entity}

@app.post("/entity/add")
def create_entity():
    entity = 'new entity'
    return {"entity": entity}

@app.get("/entity/{entity_id}")
def read_item(entity_id: int):
    print(entity_id)
    return {"item_id": entity_id}

@app.post("/entity/add/")
def add_entity(entity: Entity):
    return entity

@app.get("/entity/{entity_id}/{entity_name}")
def read_entity(entity_id: int, entity_name: str):
    entity = Entity2(id=entity_id, name=entity_name)
    return entity