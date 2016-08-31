import GameConfig
import Block
import Boat
import numpy

class Board(object):
	
	def __init__(self):
		self.blocks = [[Block.Block(j,i) for i in range(GameConfig.GameConfig.constants.COLUMNS)] for j in range(GameConfig.GameConfig.constants.ROWS)]
		self.boats = [Boat.Boat(GameConfig.GameConfig.BoatType.AIRCRAFT,self.blocks[0][0],self.blocks[5][5]) for i in range(GameConfig.GameConfig.constants.NBOTS)]
		self.boatDestroyed = numpy.zeros((GameConfig.GameConfig.constants.NBOTS,), dtype=bool)
		self.boatsPlaced = False;
		self.lastMoveStatus = False;

	def placeBoats(self,boat):
		if self.boatsPlaced == False:
			
			for i in range(0,GameConfig.GameConfig.constants.NBOTS):
				self.boatDestroyed[i] = False
				startX = boat[i].startBlock.getX()
				startY = boat[i].startBlock.getY()
				endX = boat[i].endBlock.getX()
				endY = boat[i].endBlock.getY()
				boatLife = 0
				if startX == endX:
					for x in range(startY,endY):
						self.blocks[startX][x].setStatus(GameConfig.GameConfig.BlockStatus.NOT_BLASTED)
						boatLife = boatLife + 1

				if startY == endY:
					for x in range(startX,endX):
						self.blocks[x][startY].setStatus(GameConfig.GameConfig.BlockStatus.NOT_BLASTED)
						boatLife = boatLife + 1

				self.boats[i] = boat[i]
				self.boats[i].setBoatLife(boatLife)

			self.boatsPlaced = True

	def isAllBoatsBlasted(self):
		boatsBlasted = True
		for i in range(GameConfig.GameConfig.constants.NBOTS):
			if self.boatDestroyed[i] == False:
				boatsBlasted = False
				break

		return boatsBlasted

	def dropBombOnBlock(self,block):
		if(self.blocks[block.getX()][block.getY()].getStatus() == GameConfig.GameConfig.BlockStatus.VISITED or self.blocks[block.getX()][block.getY()].getStatus() == GameConfig.GameConfig.BlockStatus.BLASTED):
			self.lastMoveStatus = GameConfig.GameConfig.MoveStatus.INVALID
			return self.lastMoveStatus
		elif(self.blocks[block.getX()][block.getY()].getStatus() == GameConfig.GameConfig.BlockStatus.NOT_BLASTED):
			self.blocks[block.getX()][block.getY()].setStatus(GameConfig.GameConfig.BlockStatus.BLASTED)
			for i in range(GameConfig.GameConfig.constants.NBOTS):
				if(self.boats[i].isBoatAttacked(self.blocks[block.getX()][block.getY()])):
					self.boats[i].decrementBoatLife()
					self.lastMoveStatus = GameConfig.GameConfig.MoveStatus.HIT
					if self.boats[i].isBoatDestroyed():
						self.boatDestroyed[i] = True
					return self.lastMoveStatus
		lastMoveStatus = GameConfig.GameConfig.MoveStatus.MISS
		self.blocks[block.getX()][block.getY()].setStatus(GameConfig.GameConfig.BlockStatus.VISITED)
		return self.lastMoveStatus

	def getAllBoatsStatus(self):
		return self.boatDestroyed

	def getlastMoveStatus(self):
		return self.lastMoveStatus