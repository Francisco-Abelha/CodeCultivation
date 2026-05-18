#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plant1 = Plant("Sunflower", 180, 95)
    plant2 = Plant("Tomato plant", 120, 70)
    plant3 = Plant("Basil", 35, 40)
    plant4 = Plant("Oak Sapling", 150, 320)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
