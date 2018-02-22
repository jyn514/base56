test: install test.py base56.py
	pytest $<

install: requirements.txt
	pip install -r requirements.txt

