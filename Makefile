PYTHON_INTERPRETER = python3


requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	$(PYTHON_INTERPRETER) -m pip install -e .

requirements_devel: requirements
	$(PYTHON_INTERPRETER) -m pip install -r requirements_devel.txt

styling:
	black gameAI
	isort gameAI
	flake8 gameAI

typing:
	mypy gameAI
	

create_requirements:
	pipreqs --force --savepath requirements.txt gameAI

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Run code

run_movement:
	$(PYTHON_INTERPRETER) gameAI/main.py movement_seek