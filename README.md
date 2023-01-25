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
  - ~~無視 見た目は度外視で Microservices はどんな感じかを掴むための実装に集中~~
  - tailwindcss を npm 上で 使っ~~てみることにする~~た いい感じ

## Api

Endpoint とよぶらしい

- GET `/problems`
- POST `/problems`
- GET `/problems/{problem_id}`
- PUT `/problems/{problem_id}`
- DELETE `/problems/{problem_id}`

- GET `/records`
- POST `/records`
- GET `/records/{record_id}`

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


class Problem(BaseModel):
    id: int
    sentence: str


class Record(BaseModel):
    id: int
    actual_typing: str
    duration: int
    registered_at: datetime
```

### Note

- 変数の命名
  - 難しいっすね
  - 問題文 -> 実際に打つ文字列のこと -> `strings` だとちょっと変? -> sentence にする
  - 打ち終わった履歴を残しておきたい `History`? `Record`? -> Record に決定

- Account
  - ごちゃごちゃするのでAccount認証系は全部作成しないことにする
  - Microservice の認証は基本的に糞の山 大変面倒らしいのでもうちょい慣れてから

## Todo

- FrontEnd
  - React
    - Axios GET, POST
  - [x] tailwindcss
    - だいぶ使いやすい 他のFrameworkも触って見る価値あり
    - が、ちょっと凝ろうとするとすんごい横長になるのでどうにかする
- Backend
  - FastAPI
    - [x] DB: Model, Access, Migrations
      - DB はなるべく軽く触りたいので `SQLite` などを利用する
      - Docker云々はよくわからん
    - [x] CRUD: API
      - Update, Delete は行わないので Read をしっかり
      - Create(post) は Recodeの新規登録だけなので簡単
    - [x] Schema: Type Definition
    - [x] Models: Migrations
      - About `ORM` (Object Relation Mapping)
      - SQLAlchemy
    - [x] test
      - async な test
      - DI: Dependency Injection
