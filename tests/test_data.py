"""
    This tests the json files for accuracy
"""
import unittest
from cerp import data
import pandas as pd

class ValidData(unittest.TestCase):
    """
        This tests the cerp
    """
    
    def test_system(self):
        for topic_name in data.ELECTION_DATA:
            topic = data.ELECTION_DATA[topic_name]
            self.assertTrue(
                isinstance(
                    topic['data'],
                    pd.core.frame.DataFrame)
            )
            self.assertTrue(
                isinstance(
                    topic['meta'],
                    dict)
            )
            length, width = topic['data'].shape
            self.assertGreater(
                length,
                100,
                "['{}']['data'] should have at least 100 pricents".format(topic_name)
            )