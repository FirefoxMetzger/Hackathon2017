class Mountain:
	
	def __init__(self):
		self.game_state = 1
	
	def getNextMessage(self):
		return "Warrior in ancient times. go __Castle__ or go __Forest__."
		
	def getStateAction(self):
		return "choice"
		
	def nextState(self, action):
		if "Forest" in action:
			return "Forest"
		elif "Castle" in action:
			return "Castle"
		else:
			raise Exception("State Assertion Failed")
		
	def isVictory(self):
		return False
	
	def isDefeat(self):	
		return False
