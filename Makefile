test:
	docker compose -f local.yml run --rm pytest

pre-commit:
	docker compose -f local.yml run --rm pre-commit

build:
	docker compose -f local.yml build

run:
	docker compose -f local.yml up

.PHONY: test pre-commit build run