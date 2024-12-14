class TSet:
    def __init__(self):
        self.elements = set()

    def empty(self):
        """Опустошить"""
        self.elements.clear()

    def add(self, element):
        """Добавить"""
        self.elements.add(element)

    def remove(self, element):
        """Удалить"""
        self.elements.discard(element)

    def is_empty(self):
        """Пусто"""
        return len(self.elements) == 0

    def contains(self, element):
        """Принадлежит"""
        return element in self.elements

    def union(self, other_set):
        """Объединить"""
        new_set = TSet()
        new_set.elements.update(self.elements | other_set.elements)
        return new_set

    def difference(self, other_set):
        """Вычесть"""
        new_set = TSet()
        new_set.elements.update(self.elements - other_set.elements)
        return new_set

    def intersection(self, other_set):
        """Умножить"""
        new_set = TSet()
        new_set.elements.update(self.elements & other_set.elements)
        return new_set

    def size(self):
        """Элементов"""
        return len(self.elements)

    def get_element(self, index):
        """Элемент"""
        if not 0 <= index < self.size():
            raise IndexError("Неверный индекс")
        return list(self.elements)[index]

    def __repr__(self):
        return f"TSet({', '.join(map(str, sorted(self.elements)))})"