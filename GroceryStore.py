import random
from datetime import datetime as dt
from datetime import timedelta


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
        now = dt.now()
        min_datetime = now - timedelta(days=90)
        min_seconds_difference = (now - min_datetime).total_seconds()
        random_seconds = random.randint(0, int(min_seconds_difference))
        self.datetime = now - timedelta(seconds=random_seconds)

    def get_type(self):
        return self.__class__.__name__

    def is_fresh(self):
        pass


class Apple(Fruit):
    def __init__(self):
        super().__init__(weight_avg=150, weight_range=50, price=2, nutrit_val_protein=0.3,
                         nutrit_val_carbohydrates=13.8, nutrit_val_fat=0.2, nutrit_val_water=85.6,
                         nutrit_val_sugar=10.4, nutrit_val_fiber=2.4)

    def is_fresh(self):
        if self.datetime + timedelta(days=30) > dt.now():
            return "Fresh"
        else:
            return "Not fresh"


class Banana(Fruit):
    def __init__(self):
        super().__init__(weight_avg=200, weight_range=100, price=3, nutrit_val_protein=1.1,
                         nutrit_val_carbohydrates=22.8, nutrit_val_fat=0.3, nutrit_val_water=74.9,
                         nutrit_val_sugar=12.2, nutrit_val_fiber=2.6)

    def is_fresh(self):
        if self.datetime + timedelta(days=30) > dt.now():
            return "Fresh"
        else:
            return "Not fresh"


class Orange(Fruit):
    def __init__(self):
        super().__init__(weight_avg=300, weight_range=100, price=4, nutrit_val_protein=1.0,
                         nutrit_val_carbohydrates=8.3, nutrit_val_fat=0.2, nutrit_val_water=88.0,
                         nutrit_val_sugar=8.2, nutrit_val_fiber=2.1)

    def is_fresh(self):
        if self.datetime + timedelta(days=30) > dt.now():
            return "Fresh"
        else:
            return "Not fresh"


class Kiwi(Fruit):
    def __init__(self):
        super().__init__(weight_avg=100, weight_range=50, price=1, nutrit_val_protein=1.1,
                         nutrit_val_carbohydrates=14.7, nutrit_val_fat=0.5, nutrit_val_water=83.1,
                         nutrit_val_sugar=9.0, nutrit_val_fiber=3.0)

    def is_fresh(self):
        if self.datetime + timedelta(days=30) > dt.now():
            return "Fresh"
        else:
            return "Not fresh"


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


class GroceryStore:
    def __init__(self, basket=Basket(), balance=0.0):
        self.basket = basket
        self.balance = balance

    def sell_fruit(self, item_type):
        fruit = self.basket.remove(item_type)
        if fruit is not None:
            self.balance += fruit.price
            return fruit
        return None


class User:
    def __init__(self, balance=200):
        self.basket = Basket()
        self.balance = balance


def formatted_number(number):
    return "%.2f" % number


def pay_menu():
    total_price = user.basket.get_total_price()
    print("Total price of the basket is", formatted_number(total_price), "$")
    print("Your balance is", formatted_number(user.balance), "$")
    print("Do you want to pay for the basket?")
    print("Type 'Yes' to pay")
    print("Type 'No' to cancel")
    command = input("Enter your command: ")
    if command == "No":
        print("Payment canceled.")
        return
    if user.balance >= total_price:
        user.balance -= total_price
        user.basket.clear()
        grocery_store.balance += total_price
        print("Payment successful!")
    else:
        print("You do not have enough money to pay for the basket.")
    input("Enter to continue...")


def run_menu():
    while True:
        available_fruits = grocery_store.basket.get_fruit_types()
        print("Welcome to the GreenGrocer!")
        print("You have", formatted_number(user.balance), "$ in your account.")
        print("Type any of the following lines to perform the corresponding action:")
        print("Add <fruit> - To add a fruit to the basket")
        print("Choose <fruit> - Choose the fruit with detailed information")
        print("Remove <fruit> - To remove a fruit from the basket")
        print("Pay - To pay for the basket")
        print("Basket - To view the basket menu")
        print("Exit - To exit the program")
        print("")
        print("Available fruits: ", available_fruits)
        print("")
        print("")

        user_input = input("Enter your command: ")
        user_input = user_input.split(" ")

        command = user_input[0].capitalize()

        if command == "Exit":
            return
        elif command == "Basket":
            basket_menu(basket=user.basket)
            print("")
            print("")
            continue
        elif command == "Pay":
            pay_menu()
            print("")
            print("")
            continue
        elif command == "Add" or command == "Remove" or command == "Choose":
            fruit_name = user_input[1].capitalize()
            if command == "Add":
                fruit = grocery_store.basket.remove(item_type=fruit_name)
                if fruit is not None:
                    user.basket.add(fruit)
                    print("Fruit added to basket.")
                else:
                    print("The fruit you requested is not available.")
            elif command == "Remove":
                fruit = user.basket.remove(item_type=fruit_name)
                if fruit is not None:
                    grocery_store.basket.add(fruit)
                    print("Fruit removed from basket.")
                else:
                    print("The fruit you requested is not in your basket.")
            elif command == "Choose":
                print("Choose", fruit_name, "from the basket via entering the index of the fruit")
                print("or type 'q' to pay for the basket.")
                for index, fruit in enumerate(grocery_store.basket.items):
                    if fruit.get_type() == fruit_name:
                        print(f"{index}: Weight: {fruit.weight}g, Is fresh? {fruit.is_fresh()}")
                selection = input("Enter id:")
                if selection != "q":
                    entered_index = int(selection)
                    selected_fruit = grocery_store.basket.items[entered_index]
                    grocery_store.basket.items.remove(selected_fruit)
                    user.basket.add(selected_fruit)
                    print("Fruit added to basket.")

        else:
            print("Invalid command.")
        input("Enter to continue...")


def basket_menu(basket):
    while True:
        print("")
        print("Basket Menu")
        print("")
        print("Items in the basket: ", basket.get_formatted_items())
        print("")
        print("Type any of the following lines to perform the corresponding action:")
        print("Weight - Calculate the total weight of the basket")
        print("Price - Calculate the total price of the basket")
        print("Nutrition - Calculate the total nutrition of the basket")
        print("Exit - To exit the basket menu")
        print("")
        print("")
        command = input("Enter your command: ")

        if command == "Exit":
            return
        elif command == "Weight":
            basket_weight = basket.get_total_weight()
            if basket_weight < 1000:
                print("Total weight of the basket is", formatted_number(basket_weight), "g")
            else:
                print("Total weight of the basket is", formatted_number(basket_weight / 1000), "kg")
            print("Items in the basket: ", basket.get_formatted_items())
        elif command == "Price":
            basket_price = basket.get_total_price()
            print("Total price of the basket is", formatted_number(basket_price), "$")
            print("Items in the basket: ", basket.get_formatted_items())
        elif command == "Nutrition":
            basket_nutrition = basket.get_total_nutrition()
            print("Total nutrition of the basket is:")
            print("Protein:", formatted_number(basket_nutrition["protein"]), "g")
            print("Carbohydrates:", formatted_number(basket_nutrition["carbohydrates"]), "g")
            print("Fat:", formatted_number(basket_nutrition["fat"]), "g")
            print("Water:", formatted_number(basket_nutrition["water"]), "g")
            print("Sugar:", formatted_number(basket_nutrition["sugar"]), "g")
            print("Fiber:", formatted_number(basket_nutrition["fiber"]), "g")
            print("Items in the basket: ", basket.get_formatted_items())
        input("Enter to continue...")


def test_ovverriding():
    basket = [Apple(), Banana(), Orange(), Kiwi()]
    for item in basket:
        print(item.datetime)
        print(item.is_fresh())


if __name__ == "__main__":
    # test_ovverriding()
    grocery_basket = Basket()
    grocery_basket.add(Apple())
    grocery_basket.add(Apple())
    grocery_basket.add(Apple())
    grocery_basket.add(Apple())
    grocery_basket.add(Banana())
    grocery_basket.add(Banana())
    grocery_basket.add(Banana())
    grocery_basket.add(Orange())
    grocery_basket.add(Orange())
    grocery_basket.add(Kiwi())
    grocery_store = GroceryStore(basket=grocery_basket)

    user = User()

    run_menu()
