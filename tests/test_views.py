import unittest
import json
import cerp


class CERPTestCase(unittest.TestCase):

    def setUp(self):
        cerp.app.testing = True
        self.app = cerp.app.test_client()

    def convert_to_json(self, obj):
        return json.loads(obj.data.decode("utf-8"))

    def test_index(self):
        """ Is there an index page in the app """
        self.assertIn(b'<html>', self.app.get('/').data)

    def test_topics(self):
        """ Is there an index page in the app """
        page = self.convert_to_json(
            self.app.get('/api/topics')
        )
        self.assertTrue(page['result'])
        self.assertTrue(isinstance(page['topics'], list))

    def test_api(self):
        """ Insure the self discovery is working """
        endpoints = self.convert_to_json(self.app.get('/api'))
        self.assertIn('/', endpoints['paths'])
        self.assertIn('/api', endpoints['paths'])
        self.assertIn(
            '/api/<topic>/<precinctNum>/pie',
            endpoints['paths']
        )
        self.assertTrue(endpoints['result'])

    def test_presidential_precinct_pie(self):
        """ TEST ENDPOINT /api/<topic>/<precNum>/pie for:
        Valid Number, all, and invalid Number """

        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/2235235101/pie')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a list
        self.assertTrue(isinstance(page['data'], list))
        # data has at least 20 items
        self.assertGreater(len(page['data']), 20)
        # data items match designated shape
        for item in page['data']:
            self.assertTrue(isinstance(item, list))
            self.assertTrue(isinstance(item[0], str))
            self.assertTrue(isinstance(item[1], int))

        # Test Bad Case
        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/223523510199999/pie')
        )
        # Result was found
        self.assertFalse(page['result'])
        # data is a list
        self.assertEqual(page['data'], None)
        self.assertTrue(isinstance(page['reason'], str))

        # Test All Case
        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/all/pie')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a list
        self.assertTrue(isinstance(page['data'], list))
        # data has at least 100 items
        self.assertEqual(len(page['data']), 22)
        # data items match designated shape
        for item in page['data']:
            self.assertTrue(isinstance(item, list))
            self.assertTrue(isinstance(item[0], str))
            self.assertTrue(isinstance(item[1], int))

    def test_presidential_precinct_meta(self):
        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/2235235101/meta')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a dict
        self.assertTrue(isinstance(page['data'], dict))
        # Keys are known, and only what we expect
        keys = set(['percentTurnout', 'registeredVoters', 'totalVotes'])
        self.assertEqual(page['data'].keys(), keys)

        # values are numbers
        for item in page['data']:
            self.assertTrue(isinstance(page['data'][item], (int, float)))

        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/all/meta')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a dict
        self.assertTrue(isinstance(page['data'], dict))
        # Keys are known, and only what we expect
        keys = set(['percentTurnout', 'registeredVoters', 'totalVotes'])

        for item in page['data']:
            self.assertEqual(page['data'][item].keys(), keys)
            # values are numbers
            for sub_item in page['data'][item]:
                self.assertTrue(
                    isinstance(
                        page['data'][item][sub_item], (int, float)))

    def test_api_topic_precinctNum_valid(self):
        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/2235235101/valid')
        )
        # Result was found
        self.assertTrue(page['result'])
        self.assertTrue(page['data'])

        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/all/valid')
        )
        # Result was found
        self.assertTrue(page['result'])
        self.assertTrue(isinstance(page['data'], list))

    def test_api_topic_precinctNum_diff(self):
        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/2235235101/diff?comp1=Clinton/Kaine&comp2=Trump/Pence')
        )
        # Result was found
        self.assertTrue(page['result'])
        self.assertTrue(page['data'])

        page = self.convert_to_json(
            self.app.get('/api/Presidential Election-2016/all/diff?comp1=Clinton/Kaine&comp2=Trump/Pence')
        )
        # Result was found
        self.assertTrue(page['result'])
        self.assertTrue(isinstance(page['data'], dict))

    def test_404_500(self):
        self.assertFalse(
            self.convert_to_json(
                self.app.get('/api/not_an_endpoint'))['result'])

        try:
            self.app.get('/api/Presidential Election-2016/dasfasdfa/meta')
            self.assertTrue(False, "Should be invalid endpoint")
        except KeyError as e:
            self.assertIn("dasfasdfa", str(e))

