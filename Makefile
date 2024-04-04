pip-compile:
	uv pip compile requirements/prod.in > requirements/prod.txt
	uv pip compile requirements/dev.in > requirements/dev.txt

up:
	docker compose -f docker-compose-dev.yaml up --build --remove-orphans --watch

down:
	docker compose -f docker-compose-dev.yaml down

cleanup:
	rm -rf .parcel-cache .mypy_cache node_modules .ruff_cache
	find . -type d -name '__pycache__' -exec rm -r {} \;
	find . -type d -name 'dist' -exec rm -r {} \;

mypy:
	mypy --strict .

format:
	ruff check --fix
	ruff format
	djlint --reformat .

lint-tpl:
	djlint --check .

lint-py:
	ruff check .