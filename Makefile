PYTHON_INTERPRETER = python3


requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	$(PYTHON_INTERPRETER) -m pip install -e .

requirements_devel:
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

run_movement_seek:
	$(PYTHON_INTERPRETER) gameAI/main.py movement_seek

run_movement_flee:
	$(PYTHON_INTERPRETER) gameAI/main.py movement_flee

run_movement_seek_arrive:
	$(PYTHON_INTERPRETER) gameAI/main.py movement_seek_arrive

run_movement_wandering:
	$(PYTHON_INTERPRETER) gameAI/main.py movement_wandering