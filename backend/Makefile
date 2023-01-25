run:
	PYTHONDONTWRITEBYTECODE=1 uvicorn api.main:app --reload

.PHONY: migrate
migrate:
	python3 -m api.migrate_db

.PHONY: docs
docs:
	google-chrome http://localhost:8000/docs

.PHONY: test
test:
	pytest -sv

.PHONY: req
req:
	pip freeze > requirements.txt
