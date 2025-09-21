from fastapi import FastAPI #this is importing fast API
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI() #this is creating the instance of FastAPI

@app.get('/blog') #decoration to define an API - Called path other languages call it routes
def index(limit=10, published: bool=True, sort: Optional[str] = None): #path operation function
    #only get 10 published blogs
    if published:
        return {
        'data': { f'{limit} published blog lists from the DB' }
    }
    else:
        return { 'data': f'{limit} blogs from the db'}

    


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'Unpublished Data'
    }

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog id = id
    return {'data': id}


@app.get('/about') #about page
def about():
    return {
        'data': 'About FastAPI'
    }

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return {'data': {'1', '2'}}



#@api -> operations decorator
#get('/') -> Path
#def about() -> Path operation functions

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post('/blog', status_code=201)
def create_blog(blog: Blog):
    return { 'data': f'Blog was created with title as {blog.title}, and here is the content: {blog.body}' }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
