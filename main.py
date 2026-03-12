from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
async def hello():
    return {'message': 'Hello Fastapi'}

@app.get('/hello')
async def hello_world():
    return HTMLResponse(f'<h1>Hello World</h1>')