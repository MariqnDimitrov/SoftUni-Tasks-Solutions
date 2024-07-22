from typing import List

from project.animals.animal import Bird

from project.food import Food


class Owl(Bird):
    ALLOWED_FOOD: List[Food] = ["Meat"]
    WEIGHT_INCREMENT = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ in self.ALLOWED_FOOD:
            self.weight += self.WEIGHT_INCREMENT * food.quantity
            self.food_eaten += food.quantity

        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    WEIGHT_INCREMENT = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += self.WEIGHT_INCREMENT * food.quantity
        self.food_eaten += food.quantity


