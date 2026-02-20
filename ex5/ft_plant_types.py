class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


class Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def __str__(self):
        return (
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """
    Child class: inherits from Plant and adds flower-specific behavior.
    """

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter} "
              f"square meters of shade")

    def __str__(self):
        return (
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """
    Child class: inherits from Plant and represents vegetables.
    Adds attributes for harvest season and nutritional value.
    """

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self):
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )

    def nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


print("=== Garden Plant Types ===")
print()
p1 = Flower("Rose", 25, 30, "red")
print(p1)
p1.bloom()
print()
p2 = Tree("Oak", 500, 1825, 50)
print(p2)
p2.produce_shade()
print()
p3 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
print(p3)
p3.nutrition()
