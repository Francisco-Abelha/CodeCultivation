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
    plant1 = Plant("Sunflower", 180, 95, 3.3)
    plant2 = Plant("Tomato plant", 120, 70, 0.1)
    plant3 = Plant("Basil", 35, 40, 2.1)
    plant4 = Plant("Oak Sapling", 150, 320, 8.6)
    plant5 = Plant("Rose", 10, 1, 0.2)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":
    main()
