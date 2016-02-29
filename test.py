import unittest

class TestStringMethods(unittest.TestCase):
    def test_bfs(self):
        import bsearch
        self.assertEqual(bsearch.bsearch(0, 10, lambda x: x >= 6), 6)

