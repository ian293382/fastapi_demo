from fastapi import FastAPI

app = FastAPI() # 先創造對象

@app.get('/helloworld')
async def read_root():
    return {'message': 'Hello, World!'}

