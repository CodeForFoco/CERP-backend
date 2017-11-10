"""
    Load all the data
"""
import json
import os
import pandas as pd



# ELECTION_DATA = {
#     "<topic>-<year>": {
#         "data": pd.
#         "meta": {}
#     }
# }

def get_voter_data():
    """
        This returns the presidental data for the 2016 election.
        Specifically a dataframe that looks like:

                     canadit | canadit   | ...
        precinctNum   votes  |   votes   | ...
        precinctNum   votes  |   votes   | ...
        ...
    """
    full_data = {}
    path = "cerp/static/microdata";
    for file in os.listdir(path=path):
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

            meta_obj = {}
            for precinct in data['precincts']:
                pnum = precinct['precinctNumber']
                del precinct["votes"]
                del precinct["precinctNumber"]
                meta_obj[pnum] = precinct
            full_data[data['topic'] + "-" + data['year']] = {}
            full_data[data['topic'] + "-" + data['year']]['data'] = final_df
            full_data[data['topic'] + "-" + data['year']]['meta'] = meta_obj    

    return full_data


# Load all
ELECTION_DATA = get_voter_data()