#!/usr/bin/env python3

class Plant:
    def __init__(
            self, name: str, height: float, age_days: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_days += 1


def main() -> None:
    plant1 = Plant("Sunflower", 180, 95, 1.5)
    count = 1
    plant_height = plant1.height
    print("=== Garden Plant Growth ===")
    plant1.show()
    while (count <= 7):
        print(f"=== Day {count} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
        count += 1
    plant_growth_done = plant1.height - plant_height
    print(f"Growth this week: {plant_growth_done}cm")


if __name__ == "__main__":
    main()
