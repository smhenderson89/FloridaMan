PYTHON ?= python3
VENV ?= .venv

.PHONY: install run

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r requirements.txt

run:
	$(VENV)/bin/python app.py
