from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "We are learning about Predifined values using Enums"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "We are still studying about predifined values using Enum class"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_name:path}")
async def read_file(file_name: str):
    return {"file_name": file_name}

