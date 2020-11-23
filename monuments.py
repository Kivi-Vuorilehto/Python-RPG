from constants import *
from random import randint


#this file is called by main when the land has been generated
#class of monument contains its position and its character on screen
# aswell as other important 

class Monument:
	monumentId = 0
	monumentLayer = Layer()
	monumentName= ""
	monumentDisplay = "M"
	monumentAmount = 0
	coord = [0, 0] # x, y

TreeHouse = Monument()
TreeHouse.monumentDisplay = "\U0001F3E1"
TreeHouse.monumentName = ""
TreeHouse.Layer = Grass
TreeHouse.monumentAmount = 5
TreeHouse.coord = []

Castle = Monument()
Castle.monumentDisplay = "\U0001F3F0"
Castle.monumentName = ""
Castle.Layer = Mountain
Castle.monumentAmount = 2
Castle.coord = []

Tree = Monument()
Tree.monumentDisplay = "\U0001F332"
Tree.monumentName= ""
Tree.Layer = Grass
Tree.monumentAmount = 50
Tree.coord = []


monumentsToGenerate = [Tree, TreeHouse, Castle]

def GetMonumentsList():
	monList = []
	for i in range(len(monumentsToGenerate)):
		for j in range(monumentsToGenerate[i].monumentAmount):
			monList.append(monumentsToGenerate[i])
	return monList
monumentsList = GetMonumentsList()



# TODO: do code


