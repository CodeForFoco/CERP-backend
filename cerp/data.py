"""
    Load all the data
"""
import json
import pandas as pd


def presidential_election_16():
    """
        This returns the presidental data for the 2016 election.
        Currently it creates then destroys a csv object, this
        step should be removed
    """
    with open("cerp/static/2016-PresidentialElection.json") as f:
        data = json.load(f)

    # Extract proper level
    a = data['precincts']

    # Convert to DataFrame and select columns we care about
    b = pd.DataFrame(a)
    c = b[['precinctNumber', 'votes']]

    # Iterate through dataframe to create list with proper associations
    result = []
    for idx, row in c.iterrows():
        for dct in row['votes']:
            dct['precinctNumber'] = row['precinctNumber']
            result.append(dct)

    # Convert back to dataframe and pivot to what you wanted
    df = pd.DataFrame(result)
    df = df.pivot(index='precinctNumber', columns='candidate', values='votes')
    return df


# Load all
PRESIDENTIAL_ELECTION_CANADITS_16 = presidential_election_16()
