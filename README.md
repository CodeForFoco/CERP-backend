# CERP

[![Build Status](https://travis-ci.org/deidyomega/CERP.svg?branch=master)](https://travis-ci.org/deidyomega/CERP)
![Coverage Status](coverage.svg)

Community Elections Resources and Polling Tool

Provide information on local elections, politicians, issues, and political outcomes. Visualize and share results.

Election information should be available to citizens in an easy to understand, fun to explore, and overall interesting way so that our community can better understand itself and its political past, present, and future.

#### Election Information

Larimer County provides information about elections at a precinct level, but the information is provided as a table of statistics. We are striving to improve the explorability of the data by building a website that lets Larimer County citizens view results on a map, compare precincts, and discover ways to reach out to elected officials.

#### Detailed Project Requirements

1. Show election information on a heat map of precincts in Larimer County.
2. Display all election outcomes for a precinct on the same page.
3. Allow different "views" of the data to be shared via hyperlinks.

## Getting Started

- TODO: Technical documentation to clone, install and run the project goes here.

This project has two parts:

A "front end" built using vue.js and a "back end" built using python+flask

Both have their own build tools and setup process.  The vuejs setup instructions are located in the `vue_builder` directory.  Be sure to be in that directory when you execute the setup steps!

As for the python application:

To get started (assuming linux or linux like)

``` bash
## Create virtual env
python3  -m venv venv #optional
. venv/bin/activate #optional
## Install Requirements
pip install --upgrade pip
pip install -r requirements.txt
sh start.sh

## Test:
sh test.sh

## Generage coverage report (and update badge):
sh coverage.sh
```

Learn more here: http://flask.pocoo.org/docs/0.12/quickstart/

A file describing what each file does is named, [DEFINTION.md](DEFINTION.md)

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

[slack]: https://codeforfoco.slack.com/
[slackinvite]: https://codeforfocoslack.herokuapp.com
[fork]: https://help.github.com/articles/fork-a-repo/
[forkthisrepo]: https://github.com/CodeForFoco/TODOUPDATEURL#fork-destination-box
[contributing]: https://github.com/CodeForFoco/org/blob/master/CONTRIBUTING.md
[githubissue]: https://github.com/CodeForFoco/TODOUPDATEURL/issues
[newissue]: https://github.com/CodeForFoco/TODOUPDATEURL/issues/new
[pullrequest]: https://github.com/CodeForFoco/TODOUPDATEURL/pulls

