class Plant:
    def __init__(self, name, height_cm=0):
        self.name = name
        self.height_cm = height_cm

    def grow(self, cm=1):
        self.height_cm += cm
        print(f"{self.name} grew {cm}cm")

    def describe(self):
        return f"{self.name}: {self.height_cm}cm"

    def kind(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height_cm=0, color="unknown", blooming=True):
        super().__init__(name, height_cm)
        self.color = color
        self.blooming = blooming

    def describe(self):
        bloom_state = "blooming" if self.blooming else "not blooming"
        return (
            f"{self.name}: {self.height_cm}cm, "
            f"{self.color} flowers ({bloom_state})")

    def kind(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height_cm=0, color="unknown", blooming=True,
                 prize_points=0):
        super().__init__(name, height_cm, color, blooming)
        self.prize_points = prize_points

    def describe(self):
        return f"{super().describe()}, Prize points: {self.prize_points}"

    def kind(self):
        return "prize"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.plants_added = 0
        self.total_growth_cm = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self, cm=1):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth_cm += cm


class GardenManager:
    class GardenStats:
        def plant_type_counts(self, garden):
            regular = 0
            flowering = 0
            prize = 0
            for p in garden.plants:
                k = p.kind()
                if k == "regular":
                    regular += 1
                elif k == "flowering":
                    flowering += 1
                else:
                    prize += 1
            return regular, flowering, prize

        def garden_score(self, garden):
            score = 0
            for p in garden.plants:
                score += p.height_cm
                if isinstance(p, PrizeFlower):
                    score += p.prize_points
            score += garden.total_growth_cm * 10
            return score

        def report(self, garden):
            print(f"\n=== {garden.owner}'s Garden Report ===")
            print("Plants in garden:")
            for p in garden.plants:
                print(f"- {p.describe()}")
            reg, flo, pri = self.plant_type_counts(garden)
            print(
                f"\nPlants added: {garden.plants_added}, "
                f"Total growth: {garden.total_growth_cm}cm")
            print(
                f"Plant types: {reg} regular, {flo} "
                f"flowering, {pri} prize flowers")

    def __init__(self):
        self.gardens = {}
        self.stats = GardenManager.GardenStats()

    def add_garden(self, garden):
        self.gardens[garden.owner] = garden

    def get_garden(self, owner):
        return self.gardens.get(owner)

    def garden_scores(self):
        scores = {}
        for owner in self.gardens:
            scores[owner] = self.stats.garden_score(self.gardens[owner])
        return scores

    @classmethod
    def create_garden_network(cls, owners):
        manager = cls()
        for owner in owners:
            manager.add_garden(Garden(owner))
        return manager

    @staticmethod
    def validate_height(height_cm):
        return 0 <= height_cm <= 10000

    def total_gardens_managed(self):
        return len(self.gardens)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice = manager.get_garden("Alice")
    bob = manager.get_garden("Bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red", True))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", True, 10))

    alice.help_all_grow(1)

    manager.stats.report(alice)
    print(
        f"\nHeight validation test: "
        f"{GardenManager.validate_height(alice.plants[0].height_cm)}")

    # Coloca plantas no Bob SEM imprimir "Added ..."
    bob.plants.append(Plant("Cactus", 90))
    bob.plants_added += 1
    bob.plants.append(FloweringPlant("Daisy", 2, "white", True))
    bob.plants_added += 1

    scores = manager.garden_scores()
    print(f"Garden scores- Alice: {scores['Alice']}, Bob: {scores['Bob']}")
    print(f"Total gardens managed: {manager.total_gardens_managed()}")
