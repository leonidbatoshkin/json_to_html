import unittest
from pj import *


class TestPJ(unittest.TestCase):

    def setUp(self):
        print('JSON file loaded')

    def test_full_convert(self):
        self.assertEqual(full_convert(data), '<h3>Title #1</h3><div>Hello, World 1!</div>')
        self.assertTrue(type(full_convert(data)) is str)
        self.assertIsNotNone(full_convert(data))

    def test_raw_html(self):
        self.assertEqual(raw_html('<>'), '&lt;&gt;')
        self.assertIn('&lt;', raw_html('>>><'))
        self.assertNotEqual(raw_html('<>'), '<>')

    def tearDown(self):
        print('The test was performed\n')


if __name__ == '__main__':
    unittest.main()
