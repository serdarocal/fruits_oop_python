import random


class Fruit:
    def __init__(self, weight_avg, weight_range, price, nutrit_val_protein, nutrit_val_carbohydrates, nutrit_val_fat,
                 nutrit_val_water,
                 nutrit_val_sugar, nutrit_val_fiber):
        self.weight = random.randint(weight_avg - weight_range, weight_avg + weight_range)
        self.price = price
        per_100g = self.weight / 100
        self.protein = nutrit_val_protein * per_100g
        self.carbohydrates = nutrit_val_carbohydrates * per_100g
        self.fat = nutrit_val_fat * per_100g
        self.water = nutrit_val_water * per_100g
        self.sugar = nutrit_val_sugar * per_100g
        self.fiber = nutrit_val_fiber * per_100g

    def get_type(self):
        return self.__class__.__name__