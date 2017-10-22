cerp/: This contains the python application (minus app.py and config.py).

docs/: This contains the original pdf's with the data used within the entire application

tests/: This (will) contain the python testing suit (unittest).

vue_builder/: This contains the "front end" of the application.  Using vuejs

.gitignore: This file tells git which other files should be ignored (build files, compiled files, cached libraries, etc)

app.py:  This is the main entry point for the application.  However while it's the entry point, it itself does nothing.

config.py: This file is used to load flask config variables as needed.  (mail, keys, etc)

DEFINITION.MD: This file describes what each file and folder contains to ease onboarding.

LICENSE: This file desribes the license we are using (MIT)

Procfile: This file is used by heroku to tell heroku how to launch our application.

README.md: This file describes the project

requirements.txt: this file lists all the python librarires that are used in this application.  It is auto generated using `pip freeze > requirements.txt`, if you add a new library, please re-execute that command to update the requirements file.  Heroku (our server) also uses this file so keeping it up to date is critial.

start.sh: Starts the python server using linux commands.  Generally speaking, it exports two environ variables, then runs flask, which uses those variables to start the application
