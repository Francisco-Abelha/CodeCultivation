#!/usr/bin/env python3

class Plant:
    def __init__(
        self, name: str, height: float, age_days: int, growth_rate: float
    ) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

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


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Sunflower", 180, 95, 3.3)
    print("Plant created: ", end="")
    plant1.show()

    plant1.set_height(200)
    plant1.set_age(19)

    plant1.set_age(-2)
    plant1.set_height(-21)

    print("Current state: ", end="")
    plant1.show()


if __name__ == "__main__":
    main()
