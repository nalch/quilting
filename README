# Quilting app
https://travis-ci.org/nalch/quilting.svg?branch=master

## Quilting backend
Make file commands::
    setup
    shell
    test
    run
    clean
    docs

## Quilting frontend
Make file commands::
    setup
    run
	test
	clean

![Build status](https://travis-ci.org/nalch/quilting.svg?branch=master)
# Quilting

> A simple management application for quilting articles

## How to run it
To setup the project the first time, simply run:
```shell
make setup
make run
```

After that, you can visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start the application.

There are users prepared to test the application:
* an administrator: `admin@nalch.de:testpassword`
* a test user: `testuser@nalch.de:testpassword`

Other useful urls are:
* Administration area: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* Api: [http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/)
* Frontend: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

# Useful Makefile commands

## Backend

### make setup
This will create the virtual environment, install the needed packages, load some sample fixtures and collect all static files.

**Be aware, that this deletes all your previous data.**

### make run
Runs the python server with the STAGE configured in the Makefile (dev by default). Feel free to configure your own stage and change some of the settings.

### make test
Installs development requirements and runs the unit tests from the test directory as well as pycodestyle and isort.

## Frontend

### make setup
Installs the client requirements (aurelia-cli) and the frontend dependencies.

**Needs node and npm installed and configured to install locally.**

### make test
Runs the frontend unit tests and eslint on the frontend's src directory.

**Run make setup to prepare the environment**

### make run
Runs the client locally with aurelia-cli in watch mode.

## Documentation

### make docs
Generate the sphinx documentation.
