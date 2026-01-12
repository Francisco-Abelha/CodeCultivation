#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

plant1 = Plant("Sunflower", 180, 95)
plant2 = Plant("Tomato plant", 120, 70)
plant3 = Plant("Basil", 35, 40)
plant4 = Plant("Oak Sapling", 150, 320)

def main():
	print("=== Garden Plant Registry ===")
	print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
	print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
	print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
	print("=== End of Program ===")


if __name__ == "__main__":
	main()

