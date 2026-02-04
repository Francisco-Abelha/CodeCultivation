#!/usr/bin/env python3

from ex1.ft_garden_data import *

def grow():
	plant1.height += 1.2
	plant2.height += 0.5
	plant3.height += 2


def age():
	plant1.age += 1
	plant2.age += 1
	plant3.age += 1

def loop():
	count = 0
	while (count < 7):
		grow()
		age()
		count += 1

def show_info():
	print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
	print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
	print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")


def main():
	print("=== Day 1 ===")
	show_info()
	loop()
	print("=== Day 7 ===")
	show_info()

if __name__ == "__main__":
	main()
