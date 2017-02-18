from Mountain import Mountain
from Town import Town
from random import random

class GameEngine:

	def __init__(self):
		self.game_state = "town"
		self.scenario = Town()
	
	def getNextMessage(self):
		return self.scenario.getNextMessage()
		
	def getStateAction(self):
		return self.scenario.getStateAction()
		
	def nextState(self, action):
		response = self.scenario.nextState(action)
	
		if self.game_state is "mountain":
			if "Forest" in response:
				self.game_state = "Forest"
				#self.scenario = Forest()
			else:
				self.game_state = "Castle"
				#self.scenario = Castle()
			
		elif self.game_state is "Forest":
			pass
		elif self.game_state is "Castle":
			pass
		else:
			#game_state is "town"
			pass
			
		
	def isVictory(self):
		if self.game_state == "Forest":
			return True
		else:
			return self.scenario.isVictory()
	
	def isDefeat(self):
		if self.game_state == "Castle":
			return True
		else:
			return self.scenario.isDefeat()

if __name__== "__main__":
	g = GameEngine()
	
	isVictory = False
	isDefeat = False
	
	while (not isDefeat and not isVictory):
		
		msg = g.getNextMessage()
		action = g.getStateAction()
		
		#DEBUG MESSAGE
		print("Scenario is: "+ g.game_state)
		print("Action is: " +action)
		print(g.scenario.game_state)
		print(msg)
		
		if action == "combat":
			next_state = input("Enter 1-4: ")
			if next_state == "1":
				next_state = "great success"
			elif next_state == "2":
				next_state = "success"
			elif next_state == "3":
				next_state = "fail"
			else:
				next_state = "epic fail"
			
			
		elif action == "choice":
			next_state = input("Enter phrase in \"__\" (double underscore): ")
			
		elif action == "SuccessRoll":
			rng = random()
			print("RNGsus gave you:"+str(rng))
			next_state = rng
			
		elif action == "none":
			next_state = 0
			 
		else:
			raise Exception("Wrong Action.")
			
		g.nextState(next_state)
		
		isVictory = g.isVictory()
		isDefeat = g.isDefeat()
		
	if isVictory:
		print(g.getNextMessage())
		print("Concrats You Win!!")
	else:
		print(g.getNextMessage())
		print("You Lose!")
