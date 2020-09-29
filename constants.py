MIN_SEED = -1000000
MAX_SEED = 1000000


WIDTH = 50
HEIGHT = 50
LAND_TO_CREATE = 1000

MIN_LAND = 4
MAX_WATER = 7
ITERATIONS = 12


#Land layers
class Layer:
    mapNum = 0
    checkWaterDistance = 3
    maxWater = 0
    display = " "
    coords = []


ZERO = "-" # water

Sand = Layer()
Sand.mapNum = 1
Sand.checkWaterDistance = 1
Sand.maxWater = 8
Sand.display = "\U0001F7E1"

Grass = Layer()
Grass.mapNum = 2
Grass.checkWaterDistance = 1
Grass.maxWater = 0
Grass.display = "\U0001F952"

Mountain = Layer()
Mountain.mapNum = 3
Mountain.checkWaterDistance = 5
Mountain.maxWater = 9
Mountain.display = "🟤"

SnowyMountain = Layer()
SnowyMountain.mapNum = 4
SnowyMountain.checkWaterDistance = 7
SnowyMountain.maxWater = 9
SnowyMountain.display = "🗻"

allLayers = [Sand, Grass, Mountain, SnowyMountain]
