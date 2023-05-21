# High Performance React Web 開発

https://www.udemy.com/share/104CFu3@vZWokXsE60n4G3KVANnZpC-AriSKQsKYryoqQERsM0zr4DuDyH3cVza4mWSKhaa1-g==/

Kazu T+さんの講座でReact QueryとReduxでTodoアプリを作ります。
このリポジトリはDjango REST Frameworkで作成したバックエンド側です。

Django REST Frameworkについては[公式サイト](https://www.django-rest-framework.org/)を確認してください。

## Pythonの環境構築

私はpyenvとvirtualenvを組み合わせて使っていますが、各自使っているPythonの環境で結構です。

```sh
brew install pyenv
brew install pyenv-virtualenv
```

pyenvで最新バージョンのPythonをインストールします。
pyenv install -lでインストールできるPythonのリストが表示されます。
私は現時点の最新である3.11.3をインストールしました。

```sh
# インストールできるPythonのリストを確認
pyenv install -l

# pythonをインストールする。
pyenv install 3.11.3

# インストールしたPythonのバージョンを確認
pyenv versions

# virtualenvを生成
pyenv virtualenv 3.11.3 fastapi
```

プロジェクトのRootディレクトリーを生成して使いたいPythonを指定します。

```sh
mkdir fast_api
cd fast_api
pyenv local fastapi
```

これでこのプロジェクトに入ると自動でPython 3.11.3の仮装環境が用意されました。

## プロジェクトの生成及びスタート

```sh
cd fast_api
pip install fastapi
pip install uvicorn
```

main.pyを作成して以下のコードを入力してください。

```python:main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

uvicornでサーバーを立ち上げます。

```sh
uvicorn main:app --reload
```

上記のFastAPIの公式サイトで詳細を確認してください。

## ライブラリーをインストールする。

pip freezeで生成したrequirements.txtを用いてライブラリーをインストールします。

```sh
pip install -r requirements.txt
```

ライブラリーを追加したり、アップデートした際にはrequirements.txtファイルを更新してください。

```sh
pip freeze > requirements.txt
```
