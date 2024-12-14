import unittest
from main import TMemory
class TestTMemory(unittest.TestCase):
    def setUp(self):
        self.memory = TMemory()
    
    def test_Store(self):
        number_to_store = 100
        self.memory.Store(number_to_store)
        self.assertEqual(self.memory.ReadNumber(), number_to_store)
        self.assertEqual(self.memory.ReadMemoryState(), 'Включена')
    
    def test_Take(self):
        number_to_store = 200
        self.memory.Store(number_to_store)
        taken_number = self.memory.Take()
        self.assertEqual(taken_number, number_to_store)
        self.assertEqual(self.memory.ReadMemoryState(), 'Включена')
    
    def test_Add(self):
        initial_number = 50
        self.memory.Store(initial_number)
        added_number = 25
        self.memory.Add(added_number)
        expected_result = initial_number + added_number
        self.assertEqual(self.memory.ReadNumber(), expected_result)
        self.assertEqual(self.memory.ReadMemoryState(), 'Включена')
        
        with self.assertRaises(TypeError):
            self.memory.Add('Некорректный аргумент')
    
    def test_Clear(self):
        self.memory.Clear()
        self.assertIsNone(self.memory.ReadNumber())
        self.assertEqual(self.memory.ReadMemoryState(), 'Выключена')
    
    def test_ReadMemoryState(self):
        self.assertEqual(self.memory.ReadMemoryState(), 'Выключена')
        self.memory.Store(123)
        self.assertEqual(self.memory.ReadMemoryState(), 'Включена')
    
    def test_ReadNumber(self):
        self.memory.Store(456)
        self.assertEqual(self.memory.ReadNumber(), 456)

    def test_Addd(self):
        initial_number = 50
        self.memory.Store(initial_number)
        added_number = '2'
        with self.assertRaises(TypeError):
            self.memory.Add(added_number)

if __name__ == '__main__':
    unittest.main()