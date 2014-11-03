#! /bin/sh

pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=3 --exclude=*.txt,*.md --max-line-length=200 .

cd UnitTest
python TestTennis.py -v
coverage run --branch TestTennis.py
coverage report -m
coverage html --title="Coverage about Tennis"
