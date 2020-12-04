import unittest

def inc(x):
    return x + 1

class cool_test(unittest.TestCase):
    def test_it(self):
    	self.assertEqual(inc(3), 4)