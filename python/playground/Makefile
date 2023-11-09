install: 
	pip install --upgrade pip && pip install -r requirements.txt
test:
	python -m pytest -vvv tests
debug:
	python -m pytest -vv --pdb
format:
	black .
lint:
	pylint --disable=R,C *.py
all:
	install lint test format