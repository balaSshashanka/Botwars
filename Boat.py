import GameConfig
import Block

class Boat(object):
	def __init__(self,bType,startBlock,endBlock):
		self.bType = bType
		self.startBlock = startBlock
		self.endBlock = endBlock
		self.boatLife = 0

	def getBoatSizeBlock(self):
		if self.startBlock.getX() == self.endBlock.getX():
			return abs(self.startBlock.getY() - self.endBlock.getY())
		else:
			return abs(self.startBlock.getX() - self.endBlock.getX())

	def isBoatAttacked(self,block):
		if(block.getX() >= startBlock.getX() and block.getX() <= endBlock.getX() and block.getY() >= startBlock.getY() and block.getY() <= endBlock.getY()):
			return True
		else:
			return False

	def isBoatInBlock(self,block):
		if block.getX() >= self.startBlock.getX() and block.getX() <= self.endBlock.getX() and block.getY() >= self.startBlock.getY() and block.getY() <= self.endBlock.getY():
			return True
		else
			return False

	def setBoatLife(self,boatLife):
		self.boatLife = boatLife

	def decrementBoatLife(self):
		self.boatLife = self.boatLife - 1

	def isBoatDestroyed(self):
		if boatLife == 0:
			return True
		else:
			return False

	def setStartBlock(self,startBlock):
		self.startBlock = startBlock

	def setEndBlock(self,endBlock):
		self.endBlock = endBlock

	def getStartBlock(self):
		return self.startBlock

	def getEndBlock(self):
		return self.endBlock