__author__ = 'vitor'

import unittest
import main


class DiamondTests(unittest.TestCase):
    def test_result_E(self):
        self.assertEqual(main.Diamond('E').result, """    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A
""")

    def test_result_C(self):
        self.assertEqual(main.Diamond('C').result, """  A
 B B
C   C
 B B
  A
""")

if __name__ == "__main__":
    unittest.main()