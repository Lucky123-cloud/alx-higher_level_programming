from fastapi import FastAPI #this is importing fast API

app = FastAPI() #this is creating the instance of FastAPI

@app.get('/') #decoration to define an API
def index() :
    return {
        'data': {'name': 'Lucky Baraka'}
    }

@app.get('/about')
def about():
    return {
        'data': 'About FastAPI'
    }