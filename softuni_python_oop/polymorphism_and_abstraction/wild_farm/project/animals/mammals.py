from typing import List

from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    ALLOWED_FOOD: List[Food] = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENT = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ in self.ALLOWED_FOOD:
            self.weight += self.WEIGHT_INCREMENT * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    ALLOWED_FOOD: List[Food] = ["Meat"]
    WEIGHT_INCREMENT = 0.4

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ in self.ALLOWED_FOOD:
            self.weight += self.WEIGHT_INCREMENT * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    ALLOWED_FOOD: List[Food] = ["Vegetable", "Meat"]
    WEIGHT_INCREMENT = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ in self.ALLOWED_FOOD:
            self.weight += self.WEIGHT_INCREMENT * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    ALLOWED_FOOD: List[Food] = ["Meat"]
    WEIGHT_INCREMENT = 1

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ in self.ALLOWED_FOOD:
            self.weight += self.WEIGHT_INCREMENT * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
