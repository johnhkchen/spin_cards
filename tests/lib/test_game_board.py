import unittest
from lib.game_board import GameBoard


class MyTestCase(unittest.TestCase):
    def test_game_board_class_exists(self):
        self.assertIsNotNone(GameBoard)  # add assertion here

    def test_game_board_instantiates(self):
        # A default game board consists of 3 concentric rings of 5 values
        # They correspond to: Attack, Defense, Health
        p1_rings = [
            [1, 1, 1, 2, 1],  # Attack
            [0, 1, 1, 1, 0],  # Defense
            [3, 4, 4, 3, 3],  # Health
        ]

        p2_rings = [
            [1, 1, 2, 1, 1],  # Attack
            [1, 0, 1, 0, 0],  # Defense
            [4, 3, 6, 3, 3],  # Health
        ]

        game_board = GameBoard(p1_rings, p2_rings)
        self.assertEqual(game_board.p1_rings, p1_rings)
        self.assertEqual(game_board.p2_rings, p2_rings)

    def test_game_board_can_rotate(self):
        # Game board should provide helper functions to rotate rings
        # usage:
        # board.rotate_ring("p1", "attack", 1, reverse=True)
        # board.rotate_ring("p2", "defense", 2)
        p1_rings = [
            [1, 1, 1, 2, 1],  # Attack
            [0, 1, 1, 1, 0],  # Defense
            [3, 4, 4, 3, 3],  # Health
        ]

        p2_rings = [
            [1, 1, 2, 1, 1],  # Attack
            [1, 0, 1, 0, 0],  # Defense
            [4, 3, 6, 3, 3],  # Health
        ]

        game_board = GameBoard(p1_rings, p2_rings)
        game_board.rotate_ring("p1", "attack", 1, reverse=True)
        game_board.rotate_ring("p2", "defense", 2)

        expected_p1_rings = [
            [1, 1, 2, 1, 1],  # Attack
            [0, 1, 1, 1, 0],  # Defense
            [3, 4, 4, 3, 3],  # Health
        ]

        expected_p2_rings = [
            [1, 1, 2, 1, 1],  # Attack
            [0, 0, 1, 0, 1],  # Defense
            [4, 3, 6, 3, 3],  # Health
        ]

        self.assertEqual(game_board.rings["p1"]["attack"].values, expected_p1_rings[0])
        self.assertEqual(game_board.rings["p1"]["defense"].values, expected_p1_rings[1])
        self.assertEqual(game_board.rings["p1"]["health"].values, expected_p1_rings[2])

        self.assertEqual(game_board.rings["p2"]["attack"].values, expected_p2_rings[0])
        self.assertEqual(game_board.rings["p2"]["defense"].values, expected_p2_rings[1])
        self.assertEqual(game_board.rings["p2"]["health"].values, expected_p2_rings[2])


if __name__ == "__main__":
    unittest.main()
