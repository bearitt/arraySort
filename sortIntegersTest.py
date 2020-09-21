import unittest
from sortInteger import sortIntegerList

class MyTestCase(unittest.TestCase):
    def test_sortInteger(self):
        self.assertEqual([1,2,3,3,6,7], sortIntegerList([7,3,6,3,2,1]))
        self.assertEqual([-5,-4,-1,2,5,7], sortIntegerList([7,-1,-4,2,5,-5]))


if __name__ == '__main__':
    unittest.main()
