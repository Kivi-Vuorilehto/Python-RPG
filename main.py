
from random import randint, seed
import time
from constants import *
from monuments import *

land = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
layerMap = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
colourMap = [[" " for j in range(WIDTH)] for i in range(HEIGHT)]
landCoordinates = []
neighbouringLand = 0
worldSeed = 0


# --- Generating Land --- #
def pprint(grid):
    print("\n" * 2)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(grid[i][j], end="  ") 
        print()		
		
def createLand() -> None:
    for i in range(LAND_TO_CREATE):
        coord = [randint(0, WIDTH - 1), randint(0, HEIGHT - 1)]
        land[coord[1]][coord[0]] = land[coord[1]][coord[0]] | 1
def cellularAutomata() -> None:
	global neighbouringLand
	coordsToWater = []
	coordsToLand = []
	for i in range(ITERATIONS):
		coordsToLand = []
		coordsToWater = []
		for y in range(HEIGHT):
			for x in range(WIDTH):
				neighbouringLand = 0
				for newY in range(-1, 2):
					for newX in range(-1, 2):
						if(newY == 0  and newX == 0):
							break
						if(y + newY >= 0  and y + newY < HEIGHT and x + newX >= 0 and x + newX < WIDTH):
							if(land[y + newY][x + newX] == 1):
								neighbouringLand += 1
				if(8 - neighbouringLand >= MAX_WATER):
					coordsToWater.append([x, y])
				elif(neighbouringLand >= MIN_LAND):
					coordsToLand.append([x, y])
		for j in range(0, len(coordsToLand) - 1):
			xCoord = coordsToLand[j][0]
			yCoord = coordsToLand[j][1]
			land[yCoord][xCoord] = 1
		for j in range(0, len(coordsToWater) - 1):
			xCoord = coordsToWater[j][0]
			yCoord = coordsToWater[j][1]
			land[yCoord][xCoord] = 0
def getLandTiles():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if(land[y][x] == 1):
                landCoordinates.append([x, y])
def getColourMap():
	surrWaterTiles = 0
	for i in range(len(allLayers)):
		for j in range(len(landCoordinates)):
			x = landCoordinates[j][0]
			y = landCoordinates[j][1]
			surrWaterTiles = 0
			for newY in range(-allLayers[i].checkWaterDistance, allLayers[i].checkWaterDistance + 1):
				for newX in range(-allLayers[i].checkWaterDistance, allLayers[i].checkWaterDistance + 1):
					if(newY == 0  and newX == 0):
						break
					if(y + newY >= 0  and y + newY < HEIGHT and x + newX >= 0 and x + newX < WIDTH):
						if(land[y + newY][x + newX] == 0):
							surrWaterTiles += 1
					else:
						surrWaterTiles += 1
			if surrWaterTiles <= allLayers[i].maxWater:
				layerMap[y][x] = allLayers[i].mapNum
def generateColourMap() -> None:
	isLand = False
	for y in range(HEIGHT):
		for x in range(WIDTH):
			isLand = False
			for i in range(0, len(allLayers)):
				if layerMap[y][x] == allLayers[i].mapNum:
					colourMap[y][x] = allLayers[i].display
					isLand = True
				if isLand == False:
					colourMap[y][x] = ZERO	
					
def generateSeed() -> None:
	global worldSeed 
	seedChoice = None
	while seedChoice != 's' and seedChoice != 'g':
	    seedChoice = input("Do you want to (g)enerate a random (s)eed or use your own?\n>>> ").lower()
	if seedChoice == 'g':
	    worldSeed = randint(MIN_SEED, MAX_SEED)
	    seed(worldSeed)
	    print(f"random seed: {worldSeed}")
	else:
		worldSeedString = int(input("Input desired seed:\n>>> "))
		string = ""
		for c in worldSeedString:
			string.append(ord(c))
		worldSeed = int(string)
	seed(worldSeed)
	
def getLayerCoordinates():
	if("\U0001F3E0" == "\U0001F952"):
		print("is same")

	for i in range(len(allLayers)):
		for y in range(HEIGHT):
			for x in range(WIDTH):
				if(str(colourMap[y][x]) == str(allLayers[i].display)):
					allLayers[i].coords.append([x , y])

# --- Genrate Monuments on Map --- #
def generateMapMonuments():
	for i in range(len(monumentsList)):
		if(len(monumentsList[i].Layer.coords) != 0):
			coordIndex = randint(0, len(monumentsList[i].Layer.coords) - 1)
			coord = monumentsList[i].Layer.coords[coordIndex]
			monumentsList[i].coord = coord
			colourMap[coord[1]][coord[0]] = monumentsList[i].monumentDisplay



# --- MAIN --- #
def main():
	#generate map
	generateSeed()
	createLand()
	cellularAutomata()

	#populate map with layers
	getLandTiles()
	getColourMap()
	generateColourMap()
	getLayerCoordinates()
	generateMapMonuments()
	pprint(colourMap)
if __name__ == "__main__":
    main()

