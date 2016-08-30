import GameConfig

class Block(object):
	def __init__(self, x , y):
		self.x = x
		self.y = y
		self.status = GameConfig.GameConfig.BlockStatus.UNTOUCHED
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y

	def getStatus(self):
		return self.status

	def setStatus(self,status):
		self.status = status

	def isBlasted(self):
		if(status == GameConfig.GameConfig.BlockStatus.BLASTED):
			return True
		else:
			return False
