from enum import Enum
from typing import Optional
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
async def get_users(page_index: int, page_size: Optional[int] = 30): 
    return {'page info': f'index: {page_index}, size: {page_size}'}

# 獲取某一個用戶的所有的朋友 /users/{user_id} ＝> 這個人的id api正常設計手段 
# 只要下面定義函數中的路徑沒有被路徑參數中定義 就是屬於查詢參數  
@app.get('/users/{user_id}/friends')
async def get_friends(page_index: int, user_id: int, page_size: Optional[int]= 10):
    return {'user_friends': f'user_id: {user_id}, indexL: {page_index}, pageSize: {page_size}'}

# 作業
@app.get('/users/{useri_id}/friends/{friend_id}')
async def get_friend_gender(user_id: int, friend_id: int, gender: Optional[Gender]= None):
    if gender is None:
        return {'friend_info': f'user_id: {user_id}, friend_id: {friend_id}, gender: Not specified'}
    else:
        return {'friend_info': f'user_id: {user_id}, friend_id: {friend_id}, gender: {gender.value}'}
# 修正不要寫 uvicorn helloworld:app -reload
if __name__ == '__main__':
    uvicorn.run(app="app:app", reload=True )
