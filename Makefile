all: quality complexity test complexity-report coverage-report

test: test-py # Run tests

test-py: unittests acceptance-tests ## Run Python tests

unittests:
	python setup.py nosetests --with-xunit --with-coverage --cover-package=configuration_py --cover-inclusive

acceptance-tests:
	coverage run -a --source='configuration_py' -m behave --tags=~@skip --format=progress3 --junit ./configuration_py/tests/acceptance/

quality: quality-py ## Run code quality checks

quality-py:
	pep8 . --format=pylint --max-line-length=140 --exclude=*/migrations/* --ignore=E121,E123,E126,E226,E24,E704,E402,W292
	pylint -f colorized central

deps-test: ## Install dependencies required to run tests
	pip install -r test_requirements.txt

complexity: ## Run code complexity checks
	xenon . -bA -mA -aA

reports: complexity-reports test-reports coverage-reports

tests-reports:
	cp nosetests.xml $(CIRCLE_TEST_REPORTS)/nosetests/
	cp -r reports $(CIRCLE_TEST_REPORTS)/behave/

complexity-report: ## Generate code complexity reports
	radon cc . -s
	radon mi . -s

coverage-report:
	coverage report
	coverage html -d $(CIRCLE_ARTIFACTS)/coverage
	codecov

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)