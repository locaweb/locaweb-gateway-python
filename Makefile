spec:
	@env PYTHONPATH=. pyvows -p '*_spec.py' --cover --cover_package=locaweb_gateway --cover_threshold=80.0 --profile specs/

setup:
	@sudo pip install --requirement=Dependencies

publish:
	python setup.py sdist upload

.PHONY: spec setup publish

