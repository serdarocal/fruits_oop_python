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


class Apple(Fruit):
    def __init__(self):
        super().__init__(weight_avg=150, weight_range=50, price=2, nutrit_val_protein=0.3,
                         nutrit_val_carbohydrates=13.8, nutrit_val_fat=0.2, nutrit_val_water=85.6,
                         nutrit_val_sugar=10.4, nutrit_val_fiber=2.4)


class Banana(Fruit):
    def __init__(self):
        super().__init__(weight_avg=200, weight_range=100, price=3, nutrit_val_protein=1.1,
                         nutrit_val_carbohydrates=22.8, nutrit_val_fat=0.3, nutrit_val_water=74.9,
                         nutrit_val_sugar=12.2, nutrit_val_fiber=2.6)


class Orange(Fruit):
    def __init__(self):
        super().__init__(weight_avg=300, weight_range=100, price=4, nutrit_val_protein=1.0,
                         nutrit_val_carbohydrates=8.3, nutrit_val_fat=0.2, nutrit_val_water=88.0,
                         nutrit_val_sugar=8.2, nutrit_val_fiber=2.1)


class Kiwi(Fruit):
    def __init__(self):
        super().__init__(weight_avg=100, weight_range=50, price=1, nutrit_val_protein=1.1,
                         nutrit_val_carbohydrates=14.7, nutrit_val_fat=0.5, nutrit_val_water=83.1,
                         nutrit_val_sugar=9.0, nutrit_val_fiber=3.0)


class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item_type):
        for item in self.items:
            if item.get_type() == item_type:
                self.items.remove(item)
                return item
        return None

    def clear(self):
        self.items = []

    def get_total_weight(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight
        return total_weight

    def get_total_nutrition(self):
        total_nutrition = {
            "protein": 0,
            "carbohydrates": 0,
            "fat": 0,
            "water": 0,
            "sugar": 0,
            "fiber": 0
        }
        for item in self.items:
            total_nutrition["protein"] += item.protein
            total_nutrition["carbohydrates"] += item.carbohydrates
            total_nutrition["fat"] += item.fat
            total_nutrition["water"] += item.water
            total_nutrition["sugar"] += item.sugar
            total_nutrition["fiber"] += item.fiber
        return total_nutrition

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

    def get_fruit_types(self):
        types = []
        for item in self.items:
            item_type = item.get_type()
            if item_type not in types:
                types.append(item_type)
        return types

    def get_formatted_items(self):
        items = {}
        for item in self.items:
            item_type = item.get_type()
            if item_type not in items:
                items[item_type] = 1
            else:
                items[item_type] += 1
        formatted_items = ""
        for item in items:
            formatted_items += str(items[item]) + "x" + item + ", "
        return formatted_items

