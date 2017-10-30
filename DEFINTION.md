[cerp/](./cerp): This contains the python application (minus [app.py](app.py) and [config.py](config.py)).

[docs/](./docs): This contains the original files with the data used within the entire application

[tests/](./tests): This contains the python testing suit (unittest).

[.gitignore](./.gitignore): This file tells git which other files should be ignored (build files, compiled files, cached libraries, etc)

[.travis.yml](.travis.yml): This file tells travis-ci.org how to build and test our project.  It needs to be improved to include vue_builder tests

[app.py](app.py):  This is the main entry point for the application.  However while it's the entry point, it itself does nothing.

[config.py](config.py): This file is used to load flask config variables as needed.  (mail, keys, etc)

[DEFINITION.MD](./DEFINITION.MD): This file describes what each file and folder contains to ease onboarding.

[LICENSE](./LICENSE): This file desribes the license we are using (MIT)

[manage.py](./manage.py): This file allows you to run, test, and show coverage of the application.  Try: `python manage.py help` for more information

[Procfile](./Procfile): This file is used by heroku to tell heroku how to launch our application.

[README.md](./README.md): This file describes the project

[requirements.txt](requirements.txt): this file lists all the python librarires that are used in this application.  It is auto generated using `pip freeze > requirements.txt`, if you add a new library, please re-execute that command to update the requirements file.  Heroku (our server) also uses this file so keeping it up to date is critial.
