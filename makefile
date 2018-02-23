.PHONY: all
all: test

.PHONY: test
test: test_codestyle test_end_to_end

.PHONY: test_end_to_end
test_end_to_end: test.py base56.py install
	pytest $<

.PHONY: test_codestyle
test_codestyle: install test.py base56.py
	pycodestyle $(filter-out install,$^)

.PHONY: install
install: .phony_install

.phony_install: requirements.txt
	touch $@
	pip install -r requirements.txt

