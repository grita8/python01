class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height = self.height + 1

    def increase_age(self):
        self.age = self.age + 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


p = Plant("Rose", 25, 30)
print("=== Day 1 ===")
p.get_info()
h1 = p.height
for i in range(6):
    p.grow()
    p.increase_age()
print("=== Day 7 ===")
p.get_info()
print(f"Growth this week: +{p.height - h1}cm")
