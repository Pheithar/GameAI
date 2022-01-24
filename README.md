# GameAI
GameAI different algorithms following Ian Millington book AI for Games third edition


I try to implememnt this algorithms using Python and `pygame`.

This project is for me, to learn how to use different GameAI algorithms and be more familiar with these algorithms.

## Usage

Python version I'm using: `python 3.10.0` 

### Makefile commands:

All the commands should be runned from the root folder.

#### General commands

`make requirements`: Install pip dependencies from the `requirements.txt`.
`make requirements_devel`: Install additional dependencies for development. Should not be necessary for running the project.
`make styling`: Fix and check sytylyng from `pep8` using `black`, `isort` and `flake8`.
`make typing`: Checks typing using `mypy`.
`make create_requirements`: Creates the `requirements.txt` file from the relevant dependencies using `pipreqs`.
`make clean`: Remove additional files such as the pycache.

#### Project commands

`make run_movement`: Run the movement algorithms


