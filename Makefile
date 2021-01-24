run:
	@docker-compose up

test:
	bin/run.sh app pytest

lint:
	bin/run.sh app flake8

format:
	bin/run.sh app black ./

build:
	@docker-compose build
