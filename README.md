# Community Elections Resources and Polling Tool (CERP)

[![Build Status](https://travis-ci.org/CodeForFoco/CERP-backend.svg?branch=master)](https://travis-ci.org/CodeForFoco/CERP-backend)
[![Coverage Status](https://coveralls.io/repos/github/CodeForFoco/CERP-backend/badge.svg)](https://coveralls.io/github/CodeForFoco/CERP-backend)

> The backend for the CERP project.
> See [CERP-webview][webview] for the frontend.

Provide information on local elections, politicians, issues, and political outcomes. Visualize and share results.

Election information should be available to citizens in an easy to understand, fun to explore, and overall interesting way so that our community can better understand itself and its political past, present, and future.

#### Election Information

Larimer County provides information about elections at a precinct level, but the information is provided as a table of statistics. We are striving to improve the explorability of the data by building a website that lets Larimer County citizens view results on a map, compare precincts, and discover ways to reach out to elected officials.

#### Detailed Project Requirements

1. Show election information on a heat map of precincts in Larimer County.
2. Display all election outcomes for a precinct on the same page.
3. Allow different "views" of the data to be shared via hyperlinks.

## Getting Started

This project has two parts:

- A **front end** built on [Vue.js][vue] and located in its [own repository][webview].  Be sure to clone that repo and follow the [setup steps][webview-setup]!
- A **back end** (this repo) built with Python + [Flask][flask].  You can learn the purpose of each file in [DEFINTION.md](DEFINTION.md).

### Initial Steps

These steps only need to be performed once.

#### Verify Required Applications

Although the `manage` application is OS-agnostic, it assumes that the current version of Python (`~3.6`) and all packages for the application are installed correctly and exist in your current `$PATH`.

#### Dependencies/Packages

To get started on a Linux or Linux-like environment (e.g. OS X), create a Python virtual environment and install the project's requirements:

```bash
python3  -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

You can read about `virtualenv` [here][virtual-env].

## Developing

Once you have completed the initial setup steps above, follow these instructions to start developing.

### Start the Server

Whenever you want to view or develop the application, activate the Python virtual environment then start the Flask server:

```bash
. venv/bin/activate
python manage.py run

# OR alternate shorthand/alias
python manage.py r
```

### Tests and Coverage Report (as needed)

To periodically run Python tests:

```bash
python manage.py test

# OR alternate shorthand/alias
python manage.py t
```

To generate a coverage report and update the `Coveralls` badge:

```bash
python manage.py coverage

# OR alternate shorthand/alias
python manage.py c 
```

## Contributing

We welcome new contributors.  Be sure to check out guide on [contributing][contributing], which includes instructions on how to fork, clone, branch, commit, pull request and sync your fork.

Not sure where to start? Look for [open issues][githubissue] on GitHub, or message the team on [our Slack site][slack]. If you aren't on our Slack, [click here for an invite][slackinvite].

TL;DR Contribution Workflow:

1. [Fork][fork] this repository and Clone your fork locally.
1. Checkout a new branch on which to make your changes.
1. Make edits. Try to match existing coding style.
1. Test your changes.
1. Commit your changes. Push your changes to your fork on GitHub.
1. Submit a new [pull request][pullrequest] and your changes will be reviewed and merged.


## Bugs / Feedback / Suggestions

We encourage you to [open up an issue][newissue] if you have any feedback, suggestions or bugs.

## License

MIT, see [LICENSE](/LICENSE) for full license.

[contributing]: https://github.com/CodeForFoco/org/blob/master/CONTRIBUTING.md
[flask]: http://flask.pocoo.org/docs/0.12/quickstart/
[fork]: https://help.github.com/articles/fork-a-repo/
[forkthisrepo]: https://github.com/CodeForFoco/CERP-backend#fork-destination-box
[githubissue]: https://github.com/CodeForFoco/CERP-backend/issues
[newissue]: https://github.com/CodeForFoco/CERP-backend/issues/new
[pullrequest]: https://github.com/CodeForFoco/CERP-backend/pulls
[slack]: https://codeforfoco.slack.com/
[slackinvite]: https://codeforfocoslack.herokuapp.com
[virtual-env]: https://pypi.python.org/pypi/virtualenv
[vue]: https://vuejs.org/
[webview-setup]: https://github.com/CodeForFoco/CERP-webview#getting-started
[webview]: https://github.com/CodeForFoco/CERP-webview