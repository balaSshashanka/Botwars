import GameConfig
import Block
import Boat
import numpy

class Board(object):
	
	def __init__(self):
		self.blocks = [[Block.Block(j,i) for i in range(GameConfig.GameConfig.constants.COLUMNS)] for j in range(GameConfig.GameConfig.constants.ROWS)]
		self.boats = [Boat.Boat(GameConfig.GameConfig.BoatType.AIRCRAFT,blocks[0][0],blocks[5][5]) for i in range(GameConfig.GameConfig.constants.NBOTS)]
		self.boatDestroyed = numpy.zeros((GameConfig.GameConfig.constants.NBOATS,), dtype=bool)
		self.boatsPlaced = False;
		self.lastMoveStatus = False;

	def placeBoats(self,boat):
		if self.boatsPlaced == False:
			for i in range(0,len(boat)):
				boatDestroyed[i] = False
				startX = boat[i].startBlock.getX()
				startY = boat[i].startBlock.getY()
				endX = boat[i].startBlock.getX()
				endY = boat[i].startBlock.getY()
				boatLife = 0

				if startX == endX:
					for x in range(startY,endY):
						blocks[x][startX].setStatus(GameConfig.GameConfig.BlockStatus.NOTBLASTED)
						boatLife = boatLife + 1

				if startY == endY:
					for x in range(startX,endX):
						blocks[x][startY].setStatus(GameConfig.GameConfig.BlockStatus.NOTBLASTED)
						boatLife = boatLife + 1

				self.boats[i] = boat[i]
				self.boats[i].setBoatLife(boatLife)

			self.boatsPlaced = True

	def isAllBoatsBlasted(self):
		boatsBlasted = True
		for i in range(len(self.boats)):
			if boatDestroyed == False:
				boatsBlasted = False
				break

		return boatsBlasted

	def dropBombOnBlock(self,block):
		if(blocks[block.getX()][block.getY()].getStatus() == GameConfig.GameConfig.BlockStatus.VISITED or blocks[block.getX()][block.getY()].getStatus() == GameConfig.GameConfig.BlockStatus.BLASTED):
			lastMoveStatus = GameConfig.GameConfig.MoveStatus.INVALID
			return lastMoveStatus
		if(blocks[block.getX,block.getY].getStatus() == GameConfig.GameConfig.BlockStatus.NOTBLASTED):
			for i in range(len(self.boats)):
				if(boats[i].isBoatAttacked(blocks[block.getX(),block.getY()])):
					boats[i].decrementBoatLife()
					self.lastMoveStatus = GameConfig.GameConfig.MoveStatus.HIT
					if boats[i].isDestroyed():
						boatDestroyed[i] = True
					return lastMoveStatus
		lastMoveStatus = GameConfig.GameConfig.MoveStatus.MISS
		blocks[block.getX()][block.getY()].setStatus(GameConfig.GameConfig.BlockStatus.VISITED)
		return lastMoveStatus

	def getAllBoatsStatus(self):
		return boatDestroyed

	def getlastMoveStatus(self):
		return lastMoveStatus