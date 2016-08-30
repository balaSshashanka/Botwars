from zope.interface import Interface

class Bot(Interface):
	
	def makeMove(self,isLastMoveHit,isBoatsDestroyed):
		'''pass'''
	def positionBoats(self,boats):
		''' pass '''