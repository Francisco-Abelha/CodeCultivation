#!/usr/bin/env python3

class Plant:
    def __init__(
        self, name: str, height: float, age_days: int
    ) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days old")

    def grow(self) -> None:
        self._height += 1

    def age(self) -> None:
        self._age_days += 1

    def set_age(self, age_days: int) -> None:
        if (age_days >= 0):
            self._age_days = age_days
            print(f"Age updated: {self._age_days}")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, height: float) -> None:
        if (height > 0):
            self._height = height
            print(f"Height updated: {self._height}")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age_days

    def get_height(self) -> float:
        return self._height


class Flower(Plant):
    def __init__(
            self, name: str, height: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        if (self._bloomed is False):
            self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if (self._bloomed):
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):

    def __init__(
            self, name: str, height: float, age_days: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age_days)
        self._nutritional_value = 0
        self._harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        return super().age()


def main() -> None:

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 10.0, 9, "Red")
    rose.show()
    print("[asking rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "Spring")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    i = 0
    while (i < 20):
        tomato.grow()
        tomato.age()
        i += 1
    tomato.show()


if __name__ == "__main__":
    main()
