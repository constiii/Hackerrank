import unittest
from magic_square import formingMagicSquare

class TestFormingMagicSquare(unittest.TestCase):
    def test_random_square_combination(self):
        """
        Testing if the formingMagicSquare function can corretly detect the cost for transforming a random square into a magic square.
        """
        s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
        
        combis = [
                 [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                 [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                 [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                 [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
                 [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                 [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
                 [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
                 [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                 ]

        result = formingMagicSquare(s, combis)

        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()