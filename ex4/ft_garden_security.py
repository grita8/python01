class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def __str__(self):
        return f"{self.name} ({self.__height}cm, {self.__age} days)"

    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height


print("=== Garden Security System ===")
p = SecurePlant("Rose", 20, 25)
p.set_height(25)
p.set_age(30)
print()
p.set_height(-5)
print()
print(f"Current plant: {p}")
