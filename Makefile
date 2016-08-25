test:
    $(shell export PYTHONPATH=$PYTHONPATH:$(pwd))
	py.test tests.py

