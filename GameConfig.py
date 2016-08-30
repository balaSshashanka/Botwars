from enum import Enum
from collections import namedtuple

class GameConfig(object):
	Constants = namedtuple('Constants',['ROWS','COLUMNS','NBOTS','USERBOT','COMPUTERBOT','BATTLESHIP_SIZE','AIRCRAFT_SIZE','SUBMARINE_SIZE','DESTROYER_SIZE','PATROL_SIZE'])
	constants = Constants(10,10,5,1,2,5,4,3,3,2)
	class BlockStatus(Enum):
		UNTOUCHED = 1
		BLASTED = 2
		NOT_BLASTED = 3
		VISITED	= 4
	class BoatType(Enum):
		BATTLESHIP = 1
		SUBMARINE = 2
		AIRCRAFT = 3
		DESTROYER = 4
		PATROL = 5
	class MoveStatus(Enum):
		HIT = 1
		MISS = 2
		INVALID = 3			