# lab14.py

# Starter code for lab 14 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Justin Le
# lej42@uci.edu
# 50644854


from abc import ABC, abstractmethod
import random

class Dog(ABC):
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
    @abstractmethod
    def breed(self):
        pass
    def age(self):
        pass
    def appetite(self):
        pass
    def hungry(self):
        pass
    def feed(self):
        pass

class Appetite:
    LOW = 3
    MEDIUM = 4
    HIGH = 5

class GermanShepherd(Dog):
    def __init__(self, name, age, appetite:Appetite=Appetite.MEDIUM):
        super().__init__(name, age)
        self._age = age
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "German Shepherd"

    def name(self):
        return self._name

    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected,
        otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0

class GoldenRetriever(Dog):
    def __init__(self, name, age, appetite:Appetite=Appetite.MEDIUM):
        super().__init__(name, age)
        self._age = age
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "Golden Retriever"

    def name(self):
        return self._name

    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected,
        otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0

class Corgi(Dog):
    def __init__(self, name, age, appetite:Appetite=Appetite.MEDIUM):
        super().__init__(name, age)
        self._age = age
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "Corgi"

    def name(self):
        return self._name

    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected,
        otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0
if __name__ == '__main__':
    dogBreed = input("Pick a dog Breed (GermanShepherd, Corgi, GoldenRetriever: ")
    dogName = input("Name your dog: ")
    if dogBreed == "GermanShepard":
        dog = GermanShepherd(dogName, 3, Appetite.HIGH)
    elif dogBreed == "Corgi":
        dog = Corgi(dogName, 3, Appetite.HIGH)
    elif dogBreed == "GoldenRetriever":
        dog = GoldenRetriever(dogName, 3, Appetite.HIGH)
    else:
        print("Error")
        quit()
    q_flag = False

    while q_flag == False:
        h_text = ""
        if dog.hungry() is False:
            h_text = "not "
        print(f"Your {dog.breed()}, {dog.name()} is {h_text}hungry.")
        feed = input(f"Would you like to feed {dog.name()}? (y/n/q): ")

        if feed == "y":
            dog.feed()
        elif feed == "q":
            break
