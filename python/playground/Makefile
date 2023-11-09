install: 
	pip install --upgrade pip && pip install -r requirements.txt
test:
	python -m pytest -vvv --cov=devopslib tests
	
debug:
	python -m pytest -vv --pdb
format:
	black *.py .
lint:
	pylint --disable=R,C *.py
all:
	install lint test format