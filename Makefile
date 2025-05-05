DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .dev.env
APP = docker_compose/app.yaml
INFRA = docker_compose/infra.yaml

.PHONY: app
app:
	${DC} -f ${APP} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP} ${ENV} down

.PHONY: infra
infra:
	${DC} -f ${INFRA} ${ENV} up --build -d

.PHONY: rabbit
rabbit:
	${DC} -f ${RABBIT} ${ENV} up --build -d

.PHONY: rabbit-down
	${DC} -f ${RABBIT} ${ENV} down
