from Mountain import Mountain
from Town import Town
from Forest import Forest
from random import random
from Castle import Castle

class GameEngine:
	def __init__(self):
		self.game_state = "Mountain"
		self.scenario = Mountain()
	
	def getNextMessage(self):
		return self.scenario.getNextMessage()
		
	def getStateAction(self):
		return self.scenario.getStateAction()
		
	def nextState(self, action):
		response = self.scenario.nextState(action)
		if self.game_state == "Mountain":
			if "Forest" == response:
				self.game_state = "Forest"
				self.scenario = Forest()
			else:
				self.game_state = "Castle"
				self.scenario = Castle()
			
		elif self.game_state == "Forest":
			if "Town" == response:
				self.game_state = "Town"
				self.scenario = Town()

		elif self.game_state == "Castle":
			if "Town" == response:
				self.game_state = "Town"
				self.scenario = Town()
		else:
			#game_state is "town"
			pass
			
		
	def isVictory(self):
		return self.scenario.isVictory()
	
	def isDefeat(self):
				return self.scenario.isDefeat()
