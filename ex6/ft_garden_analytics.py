
class Plant:
    def __init__(self, name, height) -> None:
        self.name = name
        self.init_height = height
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color) -> None:
        super().__init__(name, height)
        self.color = color

    def bloom(self) -> bool:
        if self.height > 20:
            return True

    def info(self) -> str:
        if self.bloom():
            return super().info() + f", {self.color} (blooming)"
        return super().info() + f", {self.color}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self) -> str:
        return super().info() + f", Prize points: {self.prize_points}"


class Garden():
    def __init__(self, owner, plants=[]) -> None:
        self.plants = plants
        self.owner = owner

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()


class GardenManager:
    gardens = []

    def __init__(self) -> None:
        self.gardens = []

    @classmethod
    def create_garden_network(cls, garden: Garden) -> None:
        cls.gardens.append(garden)

    @classmethod
    def total_gardens(cls) -> int:
        counter = 0
        for counter in cls.gardens:
            counter += 1
        return counter

    class GardenStats():
        def __init__(self, plants, gardens, numbers) -> None:
            self.plants = plants
            self.gardens = gardens
            self.numbers = numbers

        @staticmethod
        def garden_report(garden) -> None:
            print("Plants in garden:")
            for plant in garden.plants:
                print(plant.info())

        @staticmethod
        def growth_status(plants: list) -> None:
            len = 0
            total_growth = 0
            for plant in plants:
                len += 1
                total_growth += plant.height - plant.init_height
            print(f"\nPlants added: {len}, Total growth: {total_growth}cm")

        @staticmethod
        def plant_types(plants: list) -> None:
            n_plant = 0
            flowering = 0
            prize = 0
            for plant in plants:
                if type(plant) is Plant:
                    n_plant += 1
                elif type(plant) is FloweringPlant:
                    flowering += 1
                elif type(plant) is PrizeFlower:
                    prize += 1
            print(f"Plant types: {n_plant} regular, {flowering} flowering, \
{prize} prize flowers")

        @staticmethod
        def height_valid(plants: list) -> bool:
            for plant in plants:
                if plant.init_height < 0:
                    return False
            return True

        @staticmethod
        def garden_scores(plants: list) -> int:
            score = 0
            for plant in plants:
                if type(plant) is PrizeFlower:
                    score = score + plant.prize_points
            return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red flowers"),
        PrizeFlower("Sunflower", 50, "yellow flowers", 10)
    ]
    plants2 = [
        Plant("Oak Tree", 105),
        FloweringPlant("Rose", 23, "red flowers"),
        PrizeFlower("Magnolia", 27, "yellow flowers", 5)
    ]
    garden = Garden("Alice")
    garden2 = Garden("Bob", plants2)
    GardenManager.create_garden_network(garden)
    GardenManager.create_garden_network(garden2)
    for index in plants:
        garden.add_plant(index)

    Garden.grow_all(garden)

    print("\n=== Alice's Garden Report ===")
    GardenManager.GardenStats.garden_report(garden)
    GardenManager.GardenStats.growth_status(plants)
    GardenManager.GardenStats.plant_types(plants)

    print(f"\nHeight validation test: \
{GardenManager.GardenStats.height_valid(plants)}")
    print(f"Garden scores - Alice: \
{GardenManager.GardenStats.garden_scores(plants)}, Bob: \
{GardenManager.GardenStats.garden_scores(plants2)}")
    print(f"Total gardens managed: {len(GardenManager.gardens)}")
