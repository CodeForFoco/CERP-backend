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

    def test_api(self):
        endpoints = self.convert_to_json(self.app.get('/api'))
        self.assertIn('/', endpoints['paths'])
        self.assertIn('/api', endpoints['paths'])
        self.assertIn(
            '/api/presidential/<precinctNum>/pie',
            endpoints['paths']
        )
        self.assertTrue(endpoints['result'])

    def test_presidential_precinct_pie(self):
        page = self.convert_to_json(
            self.app.get('/api/presidential/2235235101/pie')
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

    def test_presidential_all_heatmap(self):
        page = self.convert_to_json(
            self.app.get('/api/presidential/all/heatmap')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a list
        self.assertTrue(isinstance(page['data'], dict))
        # data has at least 100 keys (key = precint)
        self.assertGreater(len(page['data']), 100)
        for item in page['data']:
            self.assertTrue(isinstance(item, str))
            self.assertTrue(isinstance(page['data'][item], str))
            self.assertIn(page['data'][item], ["#3366cc", "#dc3912"])

    def test_colorize(self):
        """ Helper function for heatmap, this just
        validates the colors haven't been switched """
        self.assertEqual(cerp.views.colorize(2, 1), "#dc3912")
        self.assertEqual(cerp.views.colorize(1, 2), "#3366cc")

    def test_presidential_all_diff(self):
        page = self.convert_to_json(
            self.app.get('/api/presidential/all/diff')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a list
        self.assertTrue(isinstance(page['data'], dict))
        # data has at least 100 keys (key = precint)
        self.assertGreater(len(page['data']), 100)
        for item in page['data']:
            self.assertTrue(isinstance(item, str))
            self.assertTrue(isinstance(page['data'][item], int))

    def test_presidential_all_pie(self):
        page = self.convert_to_json(
            self.app.get('/api/presidential/all/pie')
        )
        # Result was found
        self.assertTrue(page['result'])
        # data is a list
        self.assertTrue(isinstance(page['data'], list))
        # data has at least 100 items
        self.assertEqual(len(page['data']), 2)
        # data items match designated shape
        for item in page['data']:
            self.assertTrue(isinstance(item, list))
            self.assertTrue(isinstance(item[0], str))
            self.assertTrue(isinstance(item[1], int))
