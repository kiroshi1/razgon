.PHONY: run lint

# Запуск приложения
run:
	uv run uvicorn app.main:app --reload

# Проверка линтером Ruff
lint:
	uv run ruff check .
