from fastapi import FastAPI, Query
from typing import List
from enum import Enum

app = FastAPI()

class Model(str, Enum):
    name = "Lucky"
    age = 20
    career = "Software Engineer"

# Fake "database" of items
fake_items_db = {
    "foo": {"name": "Foo", "description": "Foo is the best item ever"},
    "bar": {"name": "Bar", "description": "Bar is also good"},
}

@app.get("/item/{item_id}")
async def read_item(item_id: int, needy: str):
    return {"item_id": item_id, "needy": needy}

@app.get("/items/{item_id}")
async def read_item_2(item_id: str, short: bool = False):
    item = fake_items_db.get(item_id, {"name": item_id, "description": "No description found"})

    if short:
        return {"item_id": item_id, "name": item["name"]}
    else:
        return {"item_id": item_id, "name": item["name"], "description": item["description"]}

# ✅ Explicitly tell FastAPI this is a query list
@app.get("/search/")
async def search(q: List[str] = Query(None)):
    return {"q": q}


@app.get("/models/{model}")
async def get_model(model: Model):
    return {"model": model}
