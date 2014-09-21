.PHONY: prepdeploy deploy ftest utest ctest test run generate check
.DEFAULT_GOAL=utest

PYTHON_CODE:=$(shell find -iname '*.py' -not -path './venv/*')
COFFEESCRIPT_CODE:=$(shell find shortanswer/static shortanswer/test_static -iname '*.coffee')

prepdeploy:
	git diff --exit-code
	git remote show heroku

deploy: prepdeploy check test
	git push heroku master
	heroku run python manage.py syncdb

test: utest ftest ctest

# unit tests
utest: $(PYTHON_CODE)
	python manage.py test shortapp.tests

# functional tests
ftest: generate
	make run > /tmp/log &
	python manage.py test functional_tests || (killall gunicorn ; false)
	killall gunicorn

# client-side tests
ctest: $(COFFEESCRIPT_CODE)
	nodeunit shortanswer/test_static

check:
	venv/bin/pylint --rcfile pylintrc shortapp

run:
	foreman start

generate:
	python manage.py syncdb
