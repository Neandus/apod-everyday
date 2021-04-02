test:
	python tests/test_modules.py
	python tests/test_package.py

test_modules:
	python tests/test_modules.py

test_package:
	python tests/test_package.py

run:
	python apod_everyday/main.py --today
