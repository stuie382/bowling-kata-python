from bowling import Bowling

import unittest


class BowlingTestSuite(unittest.TestCase):

    def setUp(self):
        self.uut = Bowling()

    def test_roll_gutter_game(self):
        self.roll([0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0])
        self.assertEqual(self.uut.score(), 0)

    def test_roll_all_ones(self):
        self.roll([1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1])
        self.assertEqual(self.uut.score(), 20)

    def test_roll_spare_followed_by_five(self):
        """
        First frame is worth 15 points, second frame adds 5
        for 20 total
        """
        self.roll([7, 3, 5, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0])
        self.assertEqual(20, self.uut.score())

    def test_roll_strike_followed_by_two_and_three(self):
        """
        As the first ball of frame one is a strike, the total
        for the frame should be the sum of the strike plus the next two rolls.

        Frame one is worth 15 points, frame 2 is worth 5 points, for 20 total
        Returns:

        """
        self.roll([10, 2, 3, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0])
        self.assertEqual(20, self.uut.score())

    def test_played_perfect_game(self):
        self.roll([10, 10, 10, 10, 10,
                   10, 10, 10, 10, 10,
                   10, 10])
        self.assertEqual(300, self.uut.score())

    def test_sample_game_scores(self):
        self.roll([1, 4, 4, 5, 6,
                   4, 5, 5, 10, 0,
                   1, 7, 3, 6, 4,
                   10, 2, 8, 6])
        self.assertEqual(133, self.uut.score())

    def roll(self, pins_down: list):
        for i in pins_down:
            self.uut.roll(i)


if __name__ == '__main__':
    unittest.main()
