import random as ra
from zope.interface import implementer

import Block
import Boat
import Bot
import GameConfig

@implementer(Bot.Bot)
class UserBot(object):
	__i = 0
	__j = 0
	def makeMove(self,isLastMoveHit,isBoatsDestroyed):
		x = self.__i
		y = self.__j
		self.__j = self.__j+1
		if(self.__j == 10):
			self.__i = self.__i + 1
			self.__j = 0
		return Block.Block(x,y)

	def positionBoats(self,boats):
		'''for i in range(5):
			pass'''

		return boats
		