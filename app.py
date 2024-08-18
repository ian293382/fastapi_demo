from enum import Enum
from fastapi import FastAPI
import uvicorn

app = FastAPI() # 先創造對象

# 建立選項類型
class Gender(str,  Enum):
    male = 'male'
    female = 'female'

@app.get('/')
async def read_root():
    return {'message': 'This is root address!'}



@app.get('/helloworld')
async def read_root():
    return {'message': 'Hello, World!'}

# 特例寫上面
@app.get('/users/current')
async def get_user():
    return {'message': f'This is  the user for current user'}   

@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return {'message': f'This is  the user for {user_id}'}   

# 建造選擇項目
@app.get('/students/{gender}')
async def get_user(gender: Gender):
    return {'message': f'This is a {gender.value} student'}   

# 建造查詢項目page_index & page_size
@app.get('/users')
async def get_users(page_index: int, page_size: int): 
    return {'page info': f'index: {page_index}, size: {page_size}'}


# 修正不要寫 uvicorn helloworld:app -reload
if __name__ == '__main__':
    uvicorn.run(app="app:app", reload=True )
