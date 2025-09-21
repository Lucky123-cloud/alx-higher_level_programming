from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="testing Out req body validation",
    docs_url= "/"
)

class User(BaseModel):
    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(gt=0, lt=100)



@app.post("/users/", status_code=201)
async def create_user(user: User):
    return {"message": f"{user.first_name} {user.last_name} has been created", "data": user}



