""" Allows for easy running of application.
 This script merely executes shell commands """
import sys
import subprocess


def run():
    """ Run the application """
    if sys.platform == 'linux' or sys.platform == 'darwin':
        subprocess.call('FLASK_APP=app.py FLASK_DEBUG=1 flask run', shell=True)
        return

    if sys.platform == 'win32':
        # Completely untested.  However as a .ps1 script it works
        subprocess.call("$env:FLASK_DEBUG = 1", shell=True)
        subprocess.call('$env:FLASK_APP = "app.py"', shell=True)
        subprocess.call("flask run", shell=True)
        return

    print("OS not known")


def coverage(auto=False):
    """ Run the coverage report """
    subprocess.call(
        'coverage run --omit=venv/* --source=cerp -m unittest discover tests/',
        shell=True)
    if not auto:
        subprocess.call('coverage html', shell=True)
        subprocess.call('xdg-open htmlcov/index.html', shell=True)


def test():
    """ Run the test suite """
    subprocess.call('python -m unittest discover tests/', shell=True)


def help_cmd():
    """ Print available commands """
    print("""
    CERP backend management tool.

    On windows assumes PowerShell
    On linux-like assumes bash (shell)

    run \t\tr \tRuns the application
    test \t\tt \tTests the application
    coverage \t\tc \tRuns the coverage report
    coverage_auto \tca \tRuns the coverage command, without showing results (for automated systems)
    help \t\th \tRuns this command

    Example:
    `python manage.py run` -- This will run the application
    """)


def manage(arg):
    """
        Grabs the arguement, and runs cmd related to it
    """
    if arg == 'help' or arg == 'h':
        help_cmd()
        return
    if arg == 'run' or arg == 'r':
        run()
        return
    if arg == 'test' or arg == 't':
        test()
        return
    if arg == 'coverage' or arg == 'c':
        coverage()
        return
    if arg == 'coverage_auto' or arg == 'ca':
        coverage(auto=True)
        return

    print("Unknown Command")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid number of arguements... showing help")
        help_cmd()
        sys.exit(1)
    manage(sys.argv[1])
