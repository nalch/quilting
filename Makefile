setup:
	cd quilting_backend && make setup
	cd quilting_frontend && make setup

test:
	cd quilting_backend && make test
	cd quilting_frontend && make test
