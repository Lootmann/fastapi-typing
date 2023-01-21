run:
	PYTHONDONTWRITEBYTECODE=1 uvicorn api.main:app --reload

.PHONY: test
test:
	pytest -sv

.PHONY: req
req:
	pip freeze > requirements.txt
