class TMemory:
    def __init__(self):
        self.FNumber = None
        self.FState = 'Выключена'
    
    def Store(self, E):
        self.FNumber = E
        self.FState = 'Включена'
        
    def Take(self):
        return self.FNumber
    
    def Add(self, E):
        if isinstance(E, type(self.FNumber)):
            self.FNumber += E
        else:
            raise TypeError("Тип аргумента не совпадает с типом хранимого числа")
        self.FState = 'Включена'
    
    def Clear(self):
        self.FNumber = None
        self.FState = 'Выключена'
        
    def ReadMemoryState(self):
        return self.FState
    
    def ReadNumber(self):
        return self.FNumber

# Примеры использования класса TMemory
if __name__ == "__main__":
    # Тестирование класса TMemory
    memory = TMemory()
    
    print(f"Состояние памяти до записи: {memory.ReadMemoryState()}")
    print(f"Число до записи: {memory.ReadNumber()}")
    
    number_to_store = 42
    memory.Store(number_to_store)
    
    print(f"Состояние памяти после записи: {memory.ReadMemoryState()}")
    print(f"Число после записи: {memory.ReadNumber()}")
    
    added_number = 10
    memory.Add(added_number)
    
    print(f"Число после добавления: {memory.ReadNumber()}")
    
    memory.Clear()
    
    print(f"Состояние памяти после очистки: {memory.ReadMemoryState()}")
    print(f"Число после очистки: {memory.ReadNumber()}")