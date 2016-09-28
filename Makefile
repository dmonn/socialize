test:
	$(shell export PYTHONPATH=$PYTHONPATH:$(pwd))
	py.test -vv tests.py
