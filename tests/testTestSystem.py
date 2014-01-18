import unittest

class TestTestSystem(unittest.TestCase):
    def test_1d_array(self):
        array = [ 1, 2, 3 ]
        self.assertEquals( 2, array[1] )

    def test_2d_array(self):
        array = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ]
        ]
        self.assertEquals( 2, array[0][1] )
