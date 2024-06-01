# Determine the home directory based on the operating system
ifeq ($(OS),Windows_NT)
	HOME_DIR := $(USERPROFILE)
	PYTHON := python
	PIP := pip
	SEP := \
	SHELL := cmd
	GO_CMD := go.bat
else
	HOME_DIR := $(HOME)
	PYTHON := python3
	PIP := pip3
	SEP := /
	GO_CMD := while true; do make run; done
endif

DIAMBRA_DIR := $(HOME_DIR)$(SEP).diambra$(SEP)roms

# Targets
run:
	diambra -r $(DIAMBRA_DIR) run -l $(PYTHON) script.py

demo:
	diambra -r $(DIAMBRA_DIR) run -l $(PYTHON) demo.py && $(PYTHON) result.py

local:
	diambra -r $(DIAMBRA_DIR) run -l $(PYTHON) ollama.py

install:
	$(PIP) install -r requirements.txt

go:
	$(GO_CMD)
