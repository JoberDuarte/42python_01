class Plant:
    def __init__(self, name: str, height: int, age_up: int) -> None:
        self.name = name
        self.height = height
        self.age_up = age_up

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_up += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_up} days old"


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(plant.get_info())

    initial_height = plant.height

    for _ in range(6):
        plant.grow()
        plant.age()

    print("=== Day 7 ===")
    print(plant.get_info())

    growth = plant.height - initial_height
    print(f"Growth this week: +{growth}cm")
