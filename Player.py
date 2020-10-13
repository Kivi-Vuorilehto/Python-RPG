import sys
from constants import *

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.inventory = {
			"Gold" : "5"
		}
	
	def move(self, dir: str) -> bool:
		if dir == "N":
			if self.y < HEIGHT - 1:
				self.y += 1
				return True
			else:
				return False
		elif dir == "W":
			if self.x > 0:
				self.x -= 1
				return True
			else:
				return False
		elif dir == "E":
			if self.x < WIDTH - 1:
				self.x += 1
				return True
			else:
				return False
		else:
			if self.y > 0:
				self.y -= 1
				return True
			else:
				return False
	
	def move_prompt(self) -> None:
		print(f"Your co-ordinates are ({self.x}, {self.y})")
		print("Where do you want to move:")
		print(
			"""
					   <8> North

			<4> West   <5> Nowhere	<6> East
					
					   <2> South
			"""
		)

		direction = 0
		while answer not in (2, 4, 5, 6, 8):
			answer = input(">>> ")
		
		if direction == 5:
			prompt()
		else:
			if direction == 2:
				while not self.move("N"):
					pass
			elif direction == 4:
				while not self.move("W"):
					pass
			elif direction == 6:
				while not self.move("E"):
					pass
			else:
				while not self.move("S"):
					pass

	def quit(self) -> None:
		sys.exit()

	def check_inventory(self) -> None:
		print("ITEM   :   QTY")
		for item in self.inventory:
			print(f"{item}   :   {inventory[item]}")
		print()

	@staticmethod
	def prompt() -> None:
		print("Here are your options:")
		print(
			"""
			<0> quit
			<1> move
			<2> inventory
			"""
		)
		answer = 0
		while answer not in range(4):
			answer = input(">>> ")
		
		if answer == 1:
			self.move_prompt()
		elif answer == 2:
			self.check_inventory()
		elif answer == 0:
			self.quit()