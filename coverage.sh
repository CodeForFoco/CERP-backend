rm .coverage
rm -r htmlcov
coverage run --omit=venv/* --source=cerp -m unittest discover tests/
coverage html
xdg-open htmlcov/index.html
coverage-badge -o coverage.svg
