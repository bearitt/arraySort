import unittest
from sortString import *

class MyTestCase(unittest.TestCase):
    def test_sortInteger(self):
        self.assertEqual(['abc','def','ghi','jkl','mno','pqr'], sortStringList([
            'def','pqr','jkl','abc','ghi','mno']))
        self.assertEqual(['Albert','Brian','Christina','Demi','Eobard','Francis'],
                sortStringList(['Demi','Francis','Eobard','Albert','Christina','Brian']))


if __name__ == '__main__':
    unittest.main()
