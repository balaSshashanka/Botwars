import random

import json
import os

import UserBot
import Board
import Boat
import GameConfig
import ComputerBot
import Block

class Controller(object):

	def __init__(self):
		self.userBot = UserBot.UserBot()
		self.computerBot = ComputerBot.ComputerBot()
		self.output = {}
		self.moves = []
		self.gameDetails = {}
		self.currentTurn = random.randrange(1,3)

	def initializeBoatArrangement(self):
		boats = [Boat.Boat(GameConfig.GameConfig.BoatType.AIRCRAFT,Block.Block(0,0),Block.Block(0,2)) for i in range(GameConfig.GameConfig.constants.NBOTS)]

		boats[0] = Boat.Boat(GameConfig.GameConfig.BoatType.AIRCRAFT,Block.Block(5,2),Block.Block(5,5))
		boats[1] = Boat.Boat(GameConfig.GameConfig.BoatType.BATTLESHIP,Block.Block(0,0),Block.Block(4,0))
		boats[2] = Boat.Boat(GameConfig.GameConfig.BoatType.SUBMARINE,Block.Block(1,9),Block.Block(3,9))
		boats[3] = Boat.Boat(GameConfig.GameConfig.BoatType.DESTROYER,Block.Block(7,2),Block.Block(9,2))
		boats[4] = Boat.Boat(GameConfig.GameConfig.BoatType.PATROL,Block.Block(7,6),Block.Block(8,6))

		return boats
	def getBoatSize(self):
		if boat.type == GameConfig.GameConfig.BoatType.AIRCRAFT:
			return GameConfig.GameConfig.constants.AIRCRAFT_SIZE
		elif boat.type == GameConfig.GameConfig.BoatType.BATTLESHIP:
			return GameConfig.GameConfig.constants.BATTLESHIP_SIZE
		elif boat.type == GameConfig.GameConfig.BoatType.DESTROYER:
			return GameConfig.GameConfig.constants.DESTROYER_SIZE
		elif boat.type == GameConfig.GameConfig.BoatType.PATROL:
			return GameConfig.GameConfig.constants.PATROL_SIZE
		elif boat.type == GameConfig.GameConfig.BoatType.SUBMARINE:
			return GameConfig.GameConfig.constants.SUBMARINE_SIZE
		else:
			return -1

	def validateBoatPosition(self,boats):
		if(len(boats) != GameConfig.GameConfig.constants.NBOTS):
			return False

		allBoatTypes = []
		for i in range(len(boats)):
			if(boats[i].type in allBoatTypes):
				return False
			allBoatTypes.append(boats[i].type)
		for i in range(len(boats)):
			if(((boats[i].getStartBlock().getX() == boats[i].getEndBlock().getX() ) or (boats[i].getStartBlock().getY() == boats[i].getEndBlock().getY())) == False):
				print('Diagonal Constraint')
				return False
			if((getBoatSize(boats[i]) == boats[i].getBoatSizeBlock()) == False):
				print('Size:' + boats[i].getBoatSizeBlock() + getBoatSize(boats[i]))
				return False
		for row in range(GameConfig.GameConfig.constants.ROWS):
			for column in range(GameConfig.GameConfig.constants.COLUMNS):
				flag = False
				for iBoat in range(len(boats)):
					if boats[iBoat].isBoatInBlock(Block.Block(row,column)):
						if flag == False:
							flag = True
						else:
							print('Overlapping')
							return False

		return True

	def start(self):
		userBoard = Board.Board()
		computerBoard = Board.Board()

		userBoats = self.initializeBoatArrangement()
		print(userBoats)
		userBoard.placeBoats(self.userBot.positionBoats(userBoats))

		uBoatList = []
		for i in range(len(userBoats)):
			boats = {}

			boats["startRow"] = userBoats[i].startBlock.getX()
			boats["startColumn"]=userBoats[i].startBlock.getY()
			boats["endRow"]=userBoats[i].endBlock.getX()
			boats["endColumn"]=userBoats[i].endBlock.getY()
			boats["Boat"]=i
			uBoatList.append(boats)
		
		computerBoats = self.initializeBoatArrangement()
		computerBoard.placeBoats(self.computerBot.positionBoats(computerBoats))

		cBotList = []
		for i in range(len(computerBoats)):
			boats = {}

			boats["startRow"]=computerBoats[i].startBlock.getX()
			boats["startColumn"]=computerBoats[i].startBlock.getY()
			boats["endRow"]=computerBoats[i].endBlock.getX()
			boats["endColumn"]=computerBoats[i].endBlock.getY()
			boats["Boat"]=i
			cBotList.append(boats)

		self.gameDetails["UserBots"] = uBoatList
		self.gameDetails["ComputerBots"] = cBotList

		self.play(userBoard,computerBoard)

		winner = self.declareWinner(userBoard, computerBoard)

		if winner == GameConfig.GameConfig.constants.USERBOT :
			print("Winner is UserBot")
		elif winner == GameConfig.GameConfig.constants.COMPUTERBOT :
			print("Winner is ComputerBot")


	def declareWinner(self,userBoard,computerBoard):
		if(userBoard.isAllBoatsBlasted()):
			return GameConfig.GameConfig.constants.COMPUTERBOT
		else:
			return GameConfig.GameConfig.constants.USERBOT

	def play(self,userBoard,computerBoard):
		while userBoard.isAllBoatsBlasted() == False and computerBoard.isAllBoatsBlasted() == False : 
			self.makeMove(userBoard, computerBoard)

	def makeMove(self,userBoard,computerBoard):
		move = {}

		if(self.currentTurn == GameConfig.GameConfig.constants.USERBOT):
			block = self.userBot.makeMove(computerBoard.getlastMoveStatus(), computerBoard.getAllBoatsStatus())
			hit = computerBoard.dropBombOnBlock(block)

			if(hit != GameConfig.GameConfig.MoveStatus.HIT):
				self.currentTurn = GameConfig.GameConfig.constants.COMPUTERBOT

			if hit != GameConfig.GameConfig.MoveStatus.INVALID:
				move["player"]="UserBot"
				move["row"]=block.getX()
				move["column"]=block.getY()
				if hit == GameConfig.GameConfig.MoveStatus.HIT:
					move["hit"]=True
				else:
					move["hit"]=False
		else:
			block = self.computerBot.makeMove(userBoard.getlastMoveStatus(), userBoard.getAllBoatsStatus())
			hit = userBoard.dropBombOnBlock(block)

			if(hit != GameConfig.GameConfig.MoveStatus.HIT):
				self.currentTurn = GameConfig.GameConfig.constants.USERBOT

			if hit != GameConfig.GameConfig.MoveStatus.INVALID:
				move["player"]="ComputerBot"
				move["row"]=block.getX()
				move["column"]=block.getY()
				if hit == GameConfig.GameConfig.MoveStatus.HIT:
					move["hit"]=True
				else:
					move["hit"]=False
		if(len(move) > 0):
			self.moves.append(move)

	def generateJSONOutput(self):
		try:
			self.output['details'] = self.gameDetails
			self.output['moves'] = self.moves
			print(self.output)
		except Exception as e:
			raise e