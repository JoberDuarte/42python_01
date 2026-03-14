class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def create_all(plant_list) -> list:
    plants = []
    for name, height, age in plant_list:
        plants.append(Plant(name, height, age))
    return plants


if __name__ == "__main__":

    plant_list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
        ]

    print("=== Plant Factory Output ===")

    plants = create_all(plant_list)

    total_plants = 0
    for p in plants:
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")
