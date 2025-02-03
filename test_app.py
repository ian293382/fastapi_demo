import pytest
from fastapi.testclient import TestClient
from app import app  # 假設你的主應用程式檔案名稱為 app.py，且裡面定義了 app 物件

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is root address!"}

def test_helloworld():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_users_current():
    response = client.get("/users/current")
    assert response.status_code == 200
    # 驗證回傳訊息中包含 "current user"
    assert "current user" in response.json().get("message", "")

def test_get_user_by_id():
    user_id = 123
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    # 驗證回傳訊息中有包含使用者 id
    assert str(user_id) in response.json().get("message", "")

def test_get_student_gender_male():
    response = client.get("/students/male")
    assert response.status_code == 200
    # 檢查回傳訊息是否包含 "male"
    assert "male" in response.json().get("message", "")

def test_get_student_gender_female():
    response = client.get("/students/female")
    assert response.status_code == 200
    # 檢查回傳訊息是否包含 "female"
    assert "female" in response.json().get("message", "")