Flaskサンプルアプリケーション
---
Herokuでの動作まで

インストール
---
Python環境およびpipenvインストール済みにして、下記実行
```bash
pipenv install
```

コマンド動作
---
```Python
pipenv run python hello.py
```

注意点
---
WSGIでサービス動作させる必要あるが、Windows環境ではGunicornが動作しない


参考URL
---
- [python - Does Gunicorn run on Windows - Stack Overflow](https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows)