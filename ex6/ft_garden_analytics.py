class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True

    def __str__(self):
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.flower_color} flowers "
                f"({bloom_status})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def __str__(self):
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.flower_color} flowers "
                f"({bloom_status}), Prize points: {self.prize_points}")


class GardenManager:
    total_gardens = 0

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1
        self.stats = self.GardenStats(self)

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def get_plant_counts(self):
            regular = flowering = prize = 0

            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

        def calculate_total_height(self):
            return sum(plant.height for plant in self.garden.plants)

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_plants_grow(self):
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            old_height = plant.height
            plant.grow()
            self.total_growth += (plant.height - old_height)

    def generate_report(self):
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")

        regular, flowering, prize = self.stats.get_plant_counts()
        total_height = self.stats.calculate_total_height()

        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

        return total_height

    @classmethod
    def create_garden_network(cls, garden_names):
        print("Creating garden network...")
        gardens = []
        for name in garden_names:
            gardens.append(cls(name))
        return gardens

    @classmethod
    def get_total_gardens(cls):
        return cls.total_gardens

    @staticmethod
    def validate_plant_height(height):
        return isinstance(height, (int, float)) and height > 0


def compare_garden_scores(garden1, garden2):
    score1 = garden1.stats.calculate_total_height()
    score2 = garden2.stats.calculate_total_height()
    print(f"Garden scores - {garden1.owner_name}: {score1}, "
          f"{garden2.owner_name}: {score2}")
    return score1, score2


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    bob_garden.add_plant(Plant("Pine Tree", 80))
    bob_garden.add_plant(FloweringPlant("Tulip", 12, "pink"))

    alice_garden.help_plants_grow()

    alice_garden.generate_report()

    print(f"Height validation test: "
          f"{GardenManager.validate_plant_height(25)}")

    compare_garden_scores(alice_garden, bob_garden)

    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
