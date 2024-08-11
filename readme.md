# 開始使用
1. python3 -m venv env # 使用venv 虛擬環境 將python3 複製到 env 的檔案資料中
2. source env/bin/activate # 使用source
3. 新增requirement.txt 將fastapi[all] 添加上去
4. pip install -r requirements.txt # 這邊會報錯通常沒有update 或有些指令去執行啊

<!-- 啟用伺服器 在 helloworld.py 這個文件下的 app object 去做物件加載  -->
5. uvicorn 高校伺服器 => $ uvicorn helloworld:app -reload

