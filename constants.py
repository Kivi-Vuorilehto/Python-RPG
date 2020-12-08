MIN_SEED = -10000000000000000000000
MAX_SEED = 10000000000000000000000


WIDTH = 30
HEIGHT = 30
LAND_TO_CREATE = round(HEIGHT * WIDTH / 2)

MIN_LAND = 4
MAX_WATER = 7
ITERATIONS = 8


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
Sand.display = "#"   
#\U000024E2
#Sand.display ="#"
Sand.coords = []

Grass = Layer()
Grass.mapNum = 2
Grass.checkWaterDistance = 1
Grass.maxWater = 0
Grass.display = "\U0001F952"
Grass.coords = []

Mountain = Layer()
Mountain.mapNum = 3
Mountain.checkWaterDistance = 7
Mountain.maxWater = 20
Mountain.display = "⛰️"
Mountain.coords = []

SnowyMountain = Layer()
SnowyMountain.mapNum = 4
SnowyMountain.checkWaterDistance = 9
SnowyMountain.maxWater = 20
SnowyMountain.display = "🗻"
SnowyMountain.coords = []

allLayers = [Sand, Grass, Mountain, SnowyMountain]
