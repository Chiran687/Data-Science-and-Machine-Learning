from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Mammal(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Mammal speaks from mammal class")

    def move(self):
        print("Mammal moves from mammal class")

    def eat(self):
        print("Mammal eats from mammal class")


class Dog(Mammal):
    def bark(self):
        print("Dog Barks (Inherited \n)")


class Bird(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Bird speaks from Bird class")

    def move(self):
        print("Bird Flies from Bird class")

    def eat(self):
        print("Bird eats from Bird class")


class Eagle(Bird):
    def fly(self):
        print("Eagle Flies Inherited \n")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Whale Whistles from Fish class")

    def move(self):
        print("Fish Swims from Fish class")

    def eat(self):
        print("Fish Feeds from Fish class")


class Salmon(Fish):
    def swim(self):
        print("Salmon swims Inherited \n")


if __name__ == "__main__":
    dog = Dog()
    eagle = Eagle()
    salmon = Salmon()

    dog.bark()
    dog.move()
    dog.eat()
    dog.speak()

    eagle.fly()
    eagle.move()
    eagle.eat()
    eagle.speak()

    salmon.swim()
    salmon.move()
    salmon.eat()
    salmon.speak()
