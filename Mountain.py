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
	message = """Imagine you are a swordsman. You have gone in many adventures 
				and this is your latest... You are now. standing on top of a
				mountain... to your left there is a dark and misty forest... 
				To your right there is an ancient castle... which way will you
				go?... To the castle?... or to the forest?..."""
	action = "choice"
	isVictory = False
	isDefeat = False

	vocabulary = ['Castle' , 'Forest']
	def nextState(self, action):
		if action == "Castle":
			return SubCastle()
		elif action == "Forest":
			return SubForest()
			
class SubForest:
	message = """You walk in to the forest.. it looks dark... ancient trees grow 
				in there... you feel as if they are looking down at you... will you 
				enter the forest or... walk along the forest."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubForest()

class SubCastle:
	message = """You have taken the path to the castle.. you come to a stop at the gate.. you can either enter the castle.. or go round and walk through the garden.. would you enter... Or go to the garden.."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubCastle()
