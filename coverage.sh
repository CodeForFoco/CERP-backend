coverage run --omit=venv/* --source=cerp -m unittest discover tests/

if [ $# -eq 1 ] && [ $1 = "--automated" ]; then
echo 'ignoring run'
else
coverage html
xdg-open htmlcov/index.html
fi
