PYTHON=python3.5

ENV_DIR=.env_$(PYTHON)
DJANGO_MANAGE=manage.py
DJANGO_SQLITE_PATH=db.sqlite3
DJANGO_SETTINGS=quilting_backend.settings

STAGE=dev

IN_ENV=. $(ENV_DIR)/bin/activate &&
WITH_SETTINGS=DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS) STAGE=$(STAGE)
# we could substitute test_project settings here
WITH_TEST_SETTINGS=DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS) STAGE=test

env:
	virtualenv -p $(PYTHON) $(ENV_DIR)

setup: clean env
	$(IN_ENV) pip install ipython
	$(IN_ENV) pip install -r requirements.txt
	$(IN_ENV) $(WITH_SETTINGS) python $(DJANGO_MANAGE) migrate
	# $(IN_ENV) $(WITH_SETTINGS) python $(DJANGO_MANAGE) loaddata initial_users.json
	# $(IN_ENV) $(WITH_SETTINGS) python $(DJANGO_MANAGE) collectstatic --clear --no-input

shell:
	$(IN_ENV) $(WITH_SETTINGS) python $(DJANGO_MANAGE) shell

dev_reqs:
	$(IN_ENV) pip install -r requirements_dev.txt

test: dev_reqs
	$(IN_ENV) $(WITH_TEST_SETTINGS) coverage run $(DJANGO_MANAGE) test
	$(IN_ENV) $(WITH_TEST_SETTINGS) pycodestyle --config .pycodestyle quilting_backend quilting_app tests
	$(IN_ENV) $(WITH_TEST_SETTINGS) isort -c -rc quilting_app quilting_backend --diff

run:
	$(IN_ENV) $(WITH_SETTINGS) python $(DJANGO_MANAGE) runserver

clean:
	rm -rf $(ENV_DIR)
	rm -f db.sqlite3
	rm -rf static

docs: dev_reqs
	$(IN_ENV) cd docs && make html
