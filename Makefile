IMAGE_NAME := telegram-bot
DOCKER_RUN := docker run --rm -v ./src/:/opt/telegram-bot ${IMAGE_NAME}


build:
	docker build --target=dev -t ${IMAGE_NAME} .
	
ruff_fix:
	${DOCKER_RUN} make ruff_fix

mypy:
	${DOCKER_RUN} make mypy