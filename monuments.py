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
	coord = [0,0] # x, y

TreeHouse = Monument()
TreeHouse.monumentDisplay = "\U0001F3E0"
TreeHouse.monumentName = ""
TreeHouse.Layer = Grass




monumentsList = [TreeHouse]
# TODO: do code


