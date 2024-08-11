from fastapi import FastAPI
import uvicorn

app = FastAPI() # 先創造對象

@app.get('/')
async def read_root():
    return {'message': 'This is root address!'}


@app.get('/helloworld')
async def read_root():
    return {'message': 'Hello, World!'}


# 修正不要寫 uvicorn helloworld:app -reload
if __name__ == '__main__':
    uvicorn.run(app="app:app", reload=True )
