"""
    Load all the data
"""
import json
import pandas as pd


def presidential_election_16():
    """
        This returns the presidental data for the 2016 election.
        Specifically a dataframe that looks like:

                     canadit | canadit   | ...
        precinctNum   votes  |   votes   | ...
        precinctNum   votes  |   votes   | ...
        ...
    """
    with open("cerp/static/2016-PresidentialElection.json") as file_handler:
        data = json.load(file_handler)

    # Convert to DataFrame and select columns we care about
    data_frame = pd.DataFrame(data['precincts'])
    data_frame = data_frame[['precinctNumber', 'votes']]

    # Iterate through dataframe to create list with proper associations
    result = []
    for _, row in data_frame.iterrows():
        for dct in row['votes']:
            dct['precinctNumber'] = row['precinctNumber']
            result.append(dct)

    # Convert back to dataframe and pivot to what you wanted
    return pd.DataFrame(result).pivot(
        index='precinctNumber',
        columns='candidate',
        values='votes')


def presidential_election_16_meta():
    """
        This loads all the meta data about the precincts
    """
    with open("cerp/static/2016-PresidentialElection.json") as file_handler:
        data = json.load(file_handler)

    meta_obj = {}
    for precinct in data['precincts']:
        pnum = precinct['precinctNumber']
        del precinct["votes"]
        del precinct["precinctNumber"]
        meta_obj[pnum] = precinct
    return meta_obj


# Load all
PRESIDENTIAL_ELECTION_CANADITS_16 = presidential_election_16()
PRESIDENTIAL_ELECTION_CANADITS_16_META = presidential_election_16_meta()
