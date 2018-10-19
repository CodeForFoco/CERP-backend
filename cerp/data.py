"""
    Load all the data
"""
import json
import os
import pandas as pd


def get_voter_data():
    """
        This is a factory that parses all provided json voter documents
        and returns them as a dictionary:

        Main dictionary format:

            ELECTION_DATA = {
                "<topic>-<year>": {
                        "data": pd.DataFrame
                        "meta": {}
                }
            }

        The "data" key has value of a pandas dataframe of the format:

                     canadit | canadit   | ...
        precinctNum   votes  |   votes   | ...
        precinctNum   votes  |   votes   | ...
        ...


        The "meta" key returns a dictionary of all meta data associated with
        the issue
    """

    full_data = {}
    path = "cerp/static/microdata"

    # Iterate through each file in the microdata directory and load its
    # contents
    for file in os.listdir(path=path):

        # Open .json only
        if file.endswith(".json"):
            with open(path + "/" + file) as file_handler:
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
            final_df = pd.DataFrame(result).pivot(
                index='precinctNumber',
                columns='candidate',
                values='votes')

            # Create the meta dictionary
            meta_obj = {}
            for precinct in data['precincts']:
                pnum = precinct['precinctNumber']
                del precinct["votes"]
                del precinct["precinctNumber"]
                meta_obj[pnum] = precinct

            sanitized_topic = data['topic'].replace(" ", "")
            # Add dataframe and meta to the full dictionary
            full_data[sanitized_topic + "-" + data['year']] = {}
            full_data[sanitized_topic + "-" + data['year']]['data'] = final_df
            full_data[sanitized_topic + "-" + data['year']]['meta'] = meta_obj

    return full_data


# Load all
ELECTION_DATA = get_voter_data()
