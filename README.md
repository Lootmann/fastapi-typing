# Typing Game

FrontEnd <-> FastAPI で作る超かんたんなゲーム

## Features

- 普通のタイピングゲーム
- 過去にタイプした記録を残しておく
  - どの程度パフォーマンスが上がったのか分析
  - `pandas` というふざけた名前のパッケージでいろいろデータを分析するらしい
  - 統計・分析の世界では デファクトスタンダードになっているくらいのとても有用なパッケージだそうで
  - 統計学の知識が必要だよ！ という訳で勉強しましょう
- HTML+CSS
  - 無視 見た目は度外視で Microservices はどんな感じかを掴むための実装に集中

## Api

Endpoint とよぶらしい

- GET `/problems`
- POST `/problems`
- GET `/problems/{problem_id}`
- GET `/records`
- POST `/records`
- GET `/records/{record_id}`

あとはアカウント系などを云々(これは後でよい)

`/problems` はすべての問題を取得する<br>
`/problems/id/` はid指定で問題を取得する<br>
こんな感じで URLをなにかの規則を持って、体系的に作っていくのが今風のAPI設計のようです<br>
`REST API` という名前がついているらしい なにかの規格?

## Model

さくっと定義

タイピングゲームで必要なのは多分これくらい

```python
from datetime import datetime
from pydantic import BaseModel


class Account(BaseModel):
    id: int
    name: str
    email: str
    password: str


class Problem(BaseModel):
    id: int
    sentence: str


class Record(BaseModel):
    id: int
    accounts: Account
    actual_typing: str
    duration: datetime.timedelta
    registered_at: datetime
```


### Note

- 変数の命名
  - 難しいっすね
  - 問題文 -> 実際に打つ文字列のこと -> `strings` だとちょっと変? -> sentence にする
  - 打ち終わった履歴を残しておきたい `History`? `Record`? -> Record に決定

## Todo

- FrontEnd
  - React
    - Axios GET, POST
- Backend
  - FastAPI
    - DB: Model, Access, Migrations
      - DB はなるべく軽く触りたいので `SQLite` などを利用する
      - Docker云々はよくわからん
    - CRUD: API
      - Update, Delete は行わないので Read をしっかり
      - Create(post) は Recodeの新規登録だけなので簡単
    - test: いろいろ
- Notation
  - Accountが実は不必要 Microservices の認証はまた別の機会に実装したほうが良いかも?
