from typing import List, Any


class Bowling:

    _rolls: List[int]

    def __init__(self):
        self._score = 0
        self._rolls = []
        self._roll_position = 0

    def roll(self, roll: int):
        """
        Add a roll to the game being played. Note that rolls must be provided
        in the correct order.
        Args:
            roll: The total number of pins knocked down by the ball
        """
        self._rolls.insert(self._roll_position, roll)
        self._roll_position += 1

    def score(self) -> int:
        """
        Calculate the total score for the game.
        Returns:    The sum of all the rolls in the game, including
                    bonus points for spares and strikes
        """
        frame_cursor = 0
        for frame in range(10):
            first_ball = self._rolls[frame_cursor]
            frame_cursor += 1
            if self._is_strike(first_ball):
                self._score += 10 + self._rolls[frame_cursor] + self._rolls[frame_cursor + 1]
                continue
            second_ball = self._rolls[frame_cursor]
            frame_cursor += 1
            if self._is_spare(first_ball, second_ball):
                self._score += 10 + self._rolls[frame_cursor]
            else:
                self._score += first_ball + second_ball

        return self._score

    @staticmethod
    def _is_strike(first: int) -> bool:
        """
        Check to see whether the first ball in a frame is a strike.
        Args:
            first: The first ball in the frame

        Returns: True if first is 10, else false

        """
        return first == 10

    @staticmethod
    def _is_spare(first: int, second: int) -> bool:
        """
        Check to see whether the frame balls add up to a spare.
        Args:
            first: The first ball in the frame
            second:  The second ball in the frame

        Returns: True if first and second sum to 10, else false

        """
        return first + second == 10
