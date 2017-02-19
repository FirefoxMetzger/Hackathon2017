class Town:
	def __init__(self):
		self.game_state = SubTown()
	
	def getNextMessage(self):
		return self.game_state.message
		
	def getStateAction(self):
		return self.game_state.action
		
	def nextState(self, action):
		new_state = self.game_state.nextState(action)
		self.game_state = new_state
		
		if isinstance(new_state,SubTown):
			return "Town"
		else:
			return "Castle"
		
	def isVictory(self):
		return self.game_state.isVictory
	
	def isDefeat(self):	
		return self.game_state.isDefeat
		
class subCasle:
	message = "You are going into an ancient castle ruin. Go inside or into garden?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "inside":
			return SubInside()
		elif action == "garden":
			return SubGarden()

class subInside:
	message = "You are inside the castle. Go upstairs, downstairs or through door?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "upstairs":
			return SubHallway()
		elif action == "door":
			return SubKitchen()
		elif action == "downstairs":
			return SubWitchLair()
	
class SubHallway:
	message = "You go upstairs into the hallway. Left door or right?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "right":
			return SubCastleGhost()
		elif action == "left":
			return SubGargoyle()

class SubCastleGhost:
	message = "You are scared and run away from the ghost."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.5:
			return SubTripAndDie()
		else:
			return SubGargoyle()
			
class SubTripAndDie:
	message = "You fall down the stairs and break your legs. you die miserably-"
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubTripAndDie()
			
class SubGargoyle:
	message = "You run into a Gargoyle. Fight or run?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "fight":
			return SubGargoyleFight()
		elif action == "run away":
			return SubGargoyleRun()
			
class SubGargoyleRun:
	message = "You try to run away."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.33:
			return SubGargoyleEscape()
		elif action < 0.66:
			return SubGargoyleRunFail()
		else:
			return SubGargoyleRunSuccess()
			
class SubGargoyleEscape:
	message = "You succeed in running away."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMaze()
			
class SubGargoyleRunFail:
	message = "You can't escape the Gargoyle slacker. You have to fight."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubGargoyleFight()
			
class SubGargoyleRunEpicFail:
	message = "You die miserably, because you are hit by a rock."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubGargoyleRunEpicFail()

class SubGargoyleFight:
	message = "You face the Gargoyle in combat"
	action = "combat"
	isVictory = False
	isDefeat = False
	
	hp = 3
	guards = 2
		
	def nextState(self, action):
		if action == "great success":
			self.guards = self.guards - 2
		elif action == "success":
			self.guards = self.guards - 1
		elif action == "fail":
			self.hp = self.hp - 1
		elif action == "epic fail":
			self.hp = self.hp - 2
		
		if self.guards <= 0:
			return SubGargoyleFightWin()
		elif self.hp <= 0:
			return SubGargoyleFightLose()
		elif self.hp == 3:
			self.message = "Very Healthy"
		elif self.hp == 2:
			self.message = "Small wound"
		elif self.hp == 1:
			self.message = "Heavily wounded"
		
		return self

class SubGargoyleFightWin:
	message = "You win the fight and exit the castle ruins."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubExitInside()	

class SubGargoyleFightLose:
	message = "You get caught between a rock and a hard place. You are dead."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubGargoyleFightLose()	
		

			
class SubKitchen:
	message = "You go straight into the kitchen. Drink or eat?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "eat":
			return SubKitchenFood()
		elif action == "drink":
			return SubKitchenDrink()

class SubKitchenFood:
	message = "The food was rotten. You die!"
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubKitchenFood()	

			
class SubWitchLair:
	message = "You find a witch lair. Fight, steal or retreat?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "fight":
			return SubSteal()
		elif action == "steal":
			return SubFight()
		elif action == "retreat":
			return SubBack()		

class subGarden:
	message = "You are in te garden. Move through flowers or towards cemetry?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "flowers":
			return SubFlowers()
		elif action == "cemetry":
			return SubCemetry()


class subTown:
