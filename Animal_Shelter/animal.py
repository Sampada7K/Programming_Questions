from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        self.animal_name = name


class Cat(Animal):
    def __init__(self, cat_name):
        super().__init__(cat_name)


class Dog(Animal):
    def __init__(self, dog_name):
        super().__init__(dog_name)
