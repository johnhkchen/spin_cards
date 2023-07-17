import unittest
from lib.ring import Ring


class MyTestCase(unittest.TestCase):
    def test_ring_class_exists(self):
        self.assertIsNotNone(Ring)  # add assertion here

    def test_ring_instantiates(self):
        # A default ring of 5 0's is created when no values are passed
        self.assertEqual(Ring().values, [0] * 5)

    def test_ring_instantiates_with_values(self):
        # Ring takes 5 numbers when being instantiated
        sample_input = [1, 2, 3, 4, 5]
        self.assertEqual(Ring(sample_input).values, sample_input)

    def test_ring_can_rotate(self):
        # Ring class takes a "rotate" command, which rotates the values "clockwise"
        sample_input = [1, 2, 3, 4, 5]
        sample_output = [5, 1, 2, 3, 4]
        ring = Ring(sample_input)
        ring.rotate()
        self.assertEqual(ring.values, sample_output)

    def test_ring_can_rotate_multiple_times(self):
        # Rotate can take a number, which rotates the values that many times
        sample_input = [1, 2, 3, 4, 5]
        sample_output = [4, 5, 1, 2, 3]
        ring = Ring(sample_input)
        ring.rotate(2)
        self.assertEqual(ring.values, sample_output)

    def test_ring_can_rotate_reversed(self):
        # with a reverse=true flag, rotate rotates the values "counter-clockwise"
        sample_input = [1, 2, 3, 4, 5]
        sample_output = [2, 3, 4, 5, 1]
        ring = Ring(sample_input)
        ring.rotate(1, reverse=True)
        self.assertEqual(ring.values, sample_output)

    def test_ring_can_rotate_reversed_multiple_times(self):
        sample_input = [1, 2, 3, 4, 5]
        sample_output = [3, 4, 5, 1, 2]
        ring = Ring(sample_input)
        ring.rotate(2, reverse=True)
        self.assertEqual(ring.values, sample_output)

    def test_ring_consecutive_rotate(self):
        sample_input = [1, 2, 3, 4, 5]
        sample_output = [3, 4, 5, 1, 2]
        ring = Ring(sample_input)
        for _ in range(8):
            ring.rotate()
        self.assertEqual(ring.values, sample_output)

    def test_ring_large_rotate(self):
        sample_input = [1, 2, 3, 4, 5]
        sample_output = [3, 4, 5, 1, 2]
        ring = Ring(sample_input)
        ring.rotate(8)
        self.assertEqual(ring.values, sample_output)

    def test_concentric_rings(self):
        read_rings = lambda rings, i: [ring.values[i] for ring in rings]
        sample_input = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
        rings = [Ring(ring) for ring in sample_input]
        self.assertEqual(read_rings(rings, 0), [1, 6])
        self.assertEqual(read_rings(rings, 1), [2, 7])
        self.assertEqual(read_rings(rings, 2), [3, 8])
        self.assertEqual(read_rings(rings, 3), [4, 9])
        self.assertEqual(read_rings(rings, 4), [5, 0])

    def test_concentric_rings_rotate(self):
        read_rings = lambda rings, i: [ring.values[i] for ring in rings]
        sample_input = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
        rings = [Ring(ring) for ring in sample_input]
        for ring in rings:
            ring.rotate(1)
        self.assertEqual(read_rings(rings, 0), [5, 0])
        self.assertEqual(read_rings(rings, 1), [1, 6])
        self.assertEqual(read_rings(rings, 2), [2, 7])
        self.assertEqual(read_rings(rings, 3), [3, 8])
        self.assertEqual(read_rings(rings, 4), [4, 9])

    def test_moderate_concentric_rings_rotate(self):
        # Time for some harder tests! Let's try 3 rings, with a ton of rotations
        # They should all be able to rotate independently
        read_rings = lambda rings, i: [ring.values[i] for ring in rings]
        sample_input = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14]]
        rings = [Ring(ring) for ring in sample_input]
        rotations = [(1, False), (2, False), (0, False)]
        for ring, rotation in zip(rings, rotations):
            ring.rotate(rotation[0], rotation[1])
        self.assertEqual(read_rings(rings, 0), [5, 9, 10])

    def test_hard_concentric_rings_rotate(self):
        read_rings = lambda rings, i: [ring.values[i] for ring in rings]
        sample_input = [[5, 3, 3, 2, 5], [-3, 2, 4, 4, 2], [12, 5, 6, 5, 8]]
        rings = [Ring(ring) for ring in sample_input]
        rotations = [(2, False), (1, False), (1, True)]
        for ring, rotation in zip(rings, rotations):
            ring.rotate(rotation[0], rotation[1])

        rotations = [(1, False), (0, False), (2, False)]
        for ring, rotation in zip(rings, rotations):
            ring.rotate(rotation[0], rotation[1])

        rotations = [(0, False), (2, False), (1, True)]
        for ring, rotation in zip(rings, rotations):
            ring.rotate(rotation[0], rotation[1])

        self.assertEqual(read_rings(rings, 0), [3, 4, 12])
        self.assertEqual(read_rings(rings, 1), [2, 4, 5])
        self.assertEqual(read_rings(rings, 2), [5, 2, 6])
        self.assertEqual(read_rings(rings, 3), [5, -3, 5])
        self.assertEqual(read_rings(rings, 4), [3, 2, 8])


if __name__ == "__main__":
    unittest.main()
