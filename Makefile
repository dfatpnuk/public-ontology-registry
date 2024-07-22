# ----------------------------------------------------------------
# public-ontology-registry
# ----------------------------------------------------------------
install:
	@echo Installing
	poetry lock --no-update
	poetry check
	poetry update
	poetry install --no-cache 
	
activate:
	@echo Activating Microservice
	poetry run dvc config core.autostage true

test:
	echo Unit Testing Microservice
	poetry run pytest --disable-pytest-warnings

freeze:
	@echo Freezing Requirements
	poetry run pip freeze > requirements.txt
	poetry run python -m pip install --upgrade pip

all:
	make install
	make freeze

jupyter:
	poetry run python -m ipykernel install --name ontology-registry
	poetry run jupyter lab

clear_cache:
	poetry cache clear --all bast-ai 