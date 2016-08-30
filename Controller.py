import random

import json
import os

import UserBot
import Board
import Boat
import GameConfig
import ComputerBot

class Controller(object):

	def __init__(self):
		self.UserBot = UserBot.UserBot()
		self.ComputerBot = ComputerBot.ComputerBot()
		self.output = {}
		self.moves = []
		self.gameDetails = json.dumps({})
		self.currentTurn = randrange(1,3)

	def initializeBoatArrangement():
		boats = [Boats.Boat() for i in range(GameConfig.GameConfig.constants.NBOTS)]

		boats[0] = Boat.Boat(GameConfig.GameConfig.BoatType.AIRCRAFT,Block.Block(0,0),Block.Block(0,2))
		boats[1] = Boat.Boat(GameConfig.GameConfig.BoatType.BATTLESHIP,Block.Block(1,3),Block.Block(4,5))
		boats[2] = Boat.Boat(GameConfig.GameConfig.BoatType.SUBMARINE,Block.Block(4,7),Block.Block(7,7))
		boats[3] = Boat.Boat(GameConfig.GameConfig.BoatType.DESTROYER,Block.Block(6,8),Block.Block(8,8))
		boats[4] = Boat.Boat(GameConfig.GameConfig.BoatType.PATROL,Block.Block(1,1),Block.Block(1,2))

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
		if(len(boats) ~= GameConfig.GameConfig.constants.NBOTS):
			return False

		allBoatTypes = []
		for i in range(len(boats)):
			if(boats[i].type in allBoatTypes):
				return False
			allBoatTypes.append(boats[i].type)
		for i in range(len(boats)):
			if(((boats[i].getStartBlock().getX() == boats[i].getEndBlock().getX() ) || (boats[i].getStartBlock().getY() == boats[i].getEndBlock().getY())) == False):
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

	def start():
		userBoard = Board.Board()
		computerBoard = Board.Board()

		userBoard = initializeBoatArrangement()
		userBoard.placeBoats(userBot.positionBoats(userBoats))

		uBoatList = []
		for i in range(len(userBoats)):
			boats = {}

			boats["startRow"] = userBoats[i].startBlock.getX()
			boats["startColumn"]=userBoats[i].startBlock.getY()
			boats["endRow"]=userBoats[i].endBlock.getX()
			boats["endColumn"]=userBoats[i].endBlock.getY()
			boats["Boat"]=i
			uBoatList.append(boats)

		computerBoats = initialBoatArrangement()
		computerBoard.placeBoats(computerBot.positionBoats(computerBoats))

		cBotList = []
		for i in range(len(computerBoats)):
			boats = {}

			boats["startRow"]=computerBoats[i].startBlock.getX()
			boats["startColumn"]=computerBoats[i].startBlock.getY()
			boats["endRow"]=computerBoats[i].endBlock.getX()
			boats["endColumn"]=computerBoats[i].endBlock.getY()
			boats["Boat"]=i
			cBoatList.append(boats)

		gameDetails.dumps("UserBots",uBoatList)
		gameDetails.dumps("ComputerBots",cBoatList)

		play(userBoard,computerBoard)

		winner = declareWinner(userBoard, computerBoard)

		if winner == GameConfig.GameConfig.constants.USERBOT :
			print("Winner is UserBot")
		else if winner == GameConfig.GameConfig.constants.COMPUTERBOT :
			print("Winner is ComputerBot")


	def declareWinner(self,userBoard,computerBoard):
		if(userBoard.isAllBoatsBlasted())
			return GameConfig.GameConfig.constants.COMPUTERBOT
		else
			return GameConfig.GameConfig.constants.USERBOT

	def play(self,userBoard,computerBoard):
		while userBoard.isAllBoatsBlasted() == False and computerBoard.isAllBoatsBlasted() == False : 
			makeMove(userBoard, computerBoard)

	def makeMove(self,userBoard,computerBoard):
		move = {}

		if(currentTurn == GameConfig.GameConfig.constants.USERBOT):
			block = userBot.makeMove(computerBoard.isLastMoveHit(), computerBoard.getAllBoatsStatus())
			hit = computerBoard.dropBombOnBlock(block)

			if(hit != GameConfig.GameConfig.MoveStatus.HIT):
				currentTurn = GameConfig.GameConfig.constants.COMPUTERBOT

			if hit != GameConfig.GameConfig.MoveStatus.INVALID:
				move["player"]="UserBot"
				move["row"]=block.getX()
				move["column"]=block.getY()
				move["hit"]=hit
		else:
			block = computerBot.makeMove(userBoard.isLastMoveHit(), userBoard.getAllBoatsStatus())
			hit = userBoard.dropBombOnBlock(block)

			if(hit != GameConfig.GameConfig.MoveStatus.HIT):
				currentTurn = GameConfig.GameConfig.constants.USERBOT

			if hit != GameConfig.GameConfig.MoveStatus.INVALID:
				move["player"]="ComputerBot"
				move["row"]=block.getX()
				move["column"]=block.getY()
				move["hit"]=hit

		moves.append(move)

	def generateJSONOutput(self):
		try:
			self.output['details'] = gameDetails
			self.output['moves'] = moves
			with open('Battleship.json', 'w') as outfile:
				print(output)
    			json.dump(output, outfile)
		except Exception, e:
			raise e