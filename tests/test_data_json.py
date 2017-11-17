"""
    This tests the json files for accuracy
"""
import unittest
import json


class ValidPrecientsPresData(unittest.TestCase):
    """
        This tests that the precients from the VoterPrecinct.geojson
        match the data from PresidentialElection.json, and that the
        data is of course valid interally.
    """

    # Start by loading the precients from the two files

    # This is from the PDF work
    with open("cerp/static/microdata/2016-PresidentialElection.json") as file_handler:
        pres_data = json.load(file_handler)
        pres_precients = [x['precinctNumber'] for x in pres_data['precincts']]

    # This is from lamier county, but it's a conversion from a .shp file
    with open("cerp/static/VoterPrecinct.geojson") as file_handler:
        geo_data = json.load(file_handler)
        geo_precients = [str(x['properties']['PRECINCT'])
                         for x in geo_data['features']]

    def test_presidential_election(self):
        """
            PresidentialElection.json precints should be unique
        """
        self.assertEqual(
            len(self.pres_precients),
            len(set(self.pres_precients)),
            "PresidentialElection.json precints should be unique"
        )

    def test_voter_precinct(self):
        """
            VoterPrecinct.geojson precints should be unique
        """
        self.assertEqual(
            len(self.geo_precients),
            len(set(self.geo_precients)),
            "VoterPrecinct.geojson precints should be unique"
        )

    def test_vp_equal_length_pe(self):
        """
            PresidentialElection.json precints should be
            the same length as VoterPrecinct.json precints
        """
        self.assertEqual(
            len(self.pres_precients),
            len(self.geo_precients),
            "PresidentialElection.json precints should be "
            "the same length as VoterPrecinct.json precints"
        )

    def test_vp_equal_pe(self):
        """
            PresidentialElection.json precints should be
            the same as VoterPrecinct.json precints
        """
        self.assertEqual(
            set(self.pres_precients),
            set(self.geo_precients),
            "PresidentialElection.json precints should be "
            "the same as VoterPrecinct.json precints"
        )
