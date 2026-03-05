class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")

    def display(self) -> None:
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade\n")

    def display(self) -> None:
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self) -> None:
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest")

    def nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "autumn", "beta carotene")

    rose.display()
    rose.bloom()

    oak.display()
    oak.produce_shade()

    tomato.display()
    tomato.nutrition()
