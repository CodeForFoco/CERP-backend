coverage run --omit=venv/* --source=cerp -m unittest discover tests/
if [ $1 != "--automated" ]; then
coverage html
xdg-open htmlcov/index.html
coverage-badge -o coverage.svg
fi
