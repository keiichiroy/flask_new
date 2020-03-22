Flaskサンプルアプリケーション
---
Waitressを用いてHerokuで動作

インストール
---
Python環境およびpipenvインストール済みにして、下記実行

```bash
pipenv install
```

コマンド動作
---
Waitressはデフォルト8080番ポートで動作

```bash
pipenv run waitress-serve --host 0.0.0.0 hello:app
```

注意点
---
- WSGIでサービス動作させる必要あるが、Windows環境ではGunicornが動作しない
- Herokuでは`pipenv install --system`が用いられるため、`Procfile`に指定するコマンドに`pipenv run`は付与しない
(ソース: https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html#deploying-system-dependencies)


参考URL
---
- [python - Does Gunicorn run on Windows - Stack Overflow](https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows)