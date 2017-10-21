"""
    Load all the data
"""
import os
import json
import csv
import pandas as pd


def presidential_election_16():
    """
        This returns the presidental data for the 2016 election.
        Currently it creates then destroys a csv object, this
        step should be removed
    """
    with open("api/static/2016-PresidentialElection.json") as f:
        data = json.load(f)

    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar="'",
            quoting=csv.QUOTE_MINIMAL)

        writer.writerow(["precinctNumber"] + sorted([x['candidate']
                                                     for x in data['precincts'][0]['votes']]))

        for row in data['precincts']:
            writer.writerow([row['precinctNumber']] + [x['votes']
                                                       for x in sorted(row['votes'], key=lambda y: y['candidate'])])

        d = pd.read_csv('data.csv', index_col="precinctNumber")
        os.remove('data.csv')  # Cleanup
        return d


# Load all
PRESIDENTIAL_ELECTION_CANADITS_16 = presidential_election_16()
