"""
    This tests the json files for accuracy
"""
import unittest
from cerp import data
import pandas as pd


class ValidPresElection16(unittest.TestCase):
    """
        This tests the cerp/data.presidential_election_16 function
        is properly creating the dataframe and it matches expected values
    """
    pres_canadits = data.presidential_election_16()

    def test_is_dataframe(self):
        """
            pres_canadits should be a dataframe
        """
        self.assertTrue(
            isinstance(
                self.pres_canadits,
                pd.core.frame.DataFrame)
        )

    def test_shape(self):
        """
            pres_canadits should match specified shape
        """
        length, width = self.pres_canadits.shape

        self.assertGreater(
            length,
            100,
            "There should be at least 100 preicents"
        )

        self.assertGreater(
            width,
            15,
            "There should be at least 15 canadits"
        )

    def test_index_name(self):
        """
            The dataframe should have an index,
            and the name is, 'precinctNumber'
        """
        self.assertEqual(
            self.pres_canadits.index.name,
            "precinctNumber"
        )
