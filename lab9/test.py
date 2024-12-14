import unittest
from main import *

class TestTSet(unittest.TestCase):
    def setUp(self):
        self.set_a = TSet()
        self.set_b = TSet()
        for i in range(1, 6):
            self.set_a.add(i)
        for i in range(3, 8):
            self.set_b.add(i)

    def test_empty(self):
        self.set_a.empty()
        self.assertTrue(self.set_a.is_empty())

    def test_add(self):
        self.set_a.add(6)
        self.assertIn(6, self.set_a.elements)

    def test_remove(self):
        self.set_a.remove(3)
        self.assertNotIn(3, self.set_a.elements)

    def test_is_empty(self):
        self.assertFalse(self.set_a.is_empty())
        self.set_a.empty()
        self.assertTrue(self.set_a.is_empty())

    def test_contains(self):
        self.assertTrue(self.set_a.contains(3))
        self.assertFalse(self.set_a.contains(6))

    def test_union(self):
        union_set = self.set_a.union(self.set_b)
        self.assertEqual(union_set.size(), 7)
        self.assertCountEqual(union_set.elements, {1, 2, 3, 4, 5, 6, 7})

    def test_difference(self):
        diff_set = self.set_a.difference(self.set_b)
        self.assertEqual(diff_set.size(), 2)
        self.assertCountEqual(diff_set.elements, {1, 2})

    def test_intersection(self):
        inter_set = self.set_a.intersection(self.set_b)
        self.assertEqual(inter_set.size(), 3)
        self.assertCountEqual(inter_set.elements, {3, 4, 5})

    def test_size(self):
        self.assertEqual(self.set_a.size(), 5)

    def test_get_element(self):
        self.assertEqual(self.set_a.get_element(0), 1)
        self.assertEqual(self.set_a.get_element(4), 5)
        with self.assertRaises(IndexError):
            self.set_a.get_element(5)

if __name__ == '__main__':
    unittest.main()