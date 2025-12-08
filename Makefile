.PHONY: run deps venv clean

VENV ?= venv
PYTHON ?= $(VENV)/bin/python
PIP ?= $(VENV)/bin/pip

venv:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip

deps: venv
	$(PIP) install -r requirements.txt

run: venv
	$(PYTHON) main.py

clean:
	rm -rf $(VENV)

