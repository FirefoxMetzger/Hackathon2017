class Mountain:
	def __init__(self):
		self.game_state = SubMountain()
	
	def getNextMessage(self):
		return self.game_state.message
		
	def getStateAction(self):
		return self.game_state.action
		
	def nextState(self, action):
		new_state = self.game_state.nextState(action)
		self.game_state = new_state
		
		if isinstance(new_state,SubForest):
			return "Forest"
		elif isinstance(new_state,SubCastle):
			return "Castle"
		
	def isVictory(self):
		return self.game_state.isVictory
	
	def isDefeat(self):	
		return self.game_state.isDefeat
		
class SubMountain:
	message = "On top of a Mountain. Forest or Castle?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "Castle":
			return SubCastle()
		elif action == "Forest":
			return SubForest()
			
class SubForest:
	message = "Going into Forest"
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubForest()

class SubCastle:
	message = "Going into Castle"
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubCastle()
