from Animal_Shelter.queue import Queue
from Animal_Shelter.animal import Cat, Dog


class AnimalQueue:
    def __init__(self):
        self.cat_q = Queue()
        self.dog_q = Queue()
        self.order = 0

    def enq_animal(self, animal: Cat or Dog):
        self.order += 1
        if isinstance(animal, Dog):
            self.dog_q.add((animal, self.order))
        elif isinstance(animal, Cat):
            self.cat_q.add((animal, self.order))
        else:
            print("Animal is neither a cat or a dog.")

    def deq_animal(self, animal_type):
        if animal_type == "dog":
            dog, dog_order = self.dog_q.delete()
            print(f"Dog order is {dog_order}")
            return dog
        elif animal_type == "cat":
            cat, cat_order = self.cat_q.delete()
            print(f"Cat order is {cat_order}")
            return cat
        else:
            print("Animal is neither a cat or a dog.")

    def deq_any(self):

        dog, dog_order = self.dog_q.peek()
        cat, cat_order = self.cat_q.peek()

        if cat_order < dog_order:
            print(f"Returning Cat since cat_order < dog_order, {cat_order} < {dog_order}")
            cat, cat_order = self.cat_q.delete()
            return cat
        else:
            print(f"Returning Dog since dog_order < cat_order, {dog_order} < {cat_order}")
            dog, dog_order = self.cat_q.delete()
            return dog


Sheeba = Cat("Sheeba")
Bagheera = Cat("Bagheera")
Archie = Dog("Archie")
Hector = Dog("Hector")

adoption_q = AnimalQueue()
adoption_q.enq_animal(Sheeba)
adoption_q.enq_animal(Bagheera)
adoption_q.enq_animal(Archie)
adoption_q.enq_animal(Hector)

print(adoption_q.deq_animal("dog"))

print(adoption_q.deq_any())

print(adoption_q.deq_animal("dog"))
print(adoption_q.deq_animal("cat"))

print(adoption_q.deq_animal("cat"))
print(adoption_q.deq_animal("dog"))




