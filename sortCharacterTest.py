import unittest
from sortCharacter import sortCharacterList

class MyTestCase(unittest.TestCase):
    def test_sortCharacter(self):
        self.assertEqual(['1','b','c','d','e','f'], sortCharacterList(['f','e','d','c','b','1']))
        self.assertEqual(['1','@','A','F','c','d'], sortCharacterList(['F','A','d','c','1','@']))


if __name__ == '__main__':
    unittest.main()
