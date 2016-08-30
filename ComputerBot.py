import random as ra
from zope.interface import implementer

import Block
import Boat
import Bot
import GameConfig

@implementer(Bot.Bot)
class ComputerBot(object):

	def makeMove(self,isLastMoveHit,isBoatsDestroyed):
		x = ra.randrange(1,GameConfig.GameConfig.constants.ROWS)
		y = ra.randrange(1,GameConfig.GameConfig.constants.COLUMNS)
		return Block.Block(x,y)

	def positionBoats(self,boats):
		for i in xrange(len(boats)):
			pass

		return boats
		