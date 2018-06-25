setup: clean
	npm install

run:
	au run -w

test:
	npm test

clean:
	rm -rf node_modules
	rm -rf dist

docs: dev_reqs
	$(IN_ENV) cd docs && make html
