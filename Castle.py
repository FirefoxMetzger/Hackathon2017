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
	message = """You have taken the path to the castle… you come to a stop at the gate… you can either enter the castle… or go round and walk through the garden… would you enter…. Or go to the garden…"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "inside":
			return SubInside()
		elif action == "garden":
			return SubGarden()

class subInside:
	message = """you push open the door… it slowly opens in… you walk inside… it seems that someone was living in the castle… you look around… when you look up you see a staircase leading up to another floor… you look around and see what looks like the kitchen… also. You see another trap door leading to what looks like the cellar… where will you go… upstairs… kitchen… or… cellar…"""
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
	message = """you climb the staircase slowly… you are careful not to make any noise… you see two doors… which one would you take… left door or right… """
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "right":
			return SubCastleGhost()
		elif action == "left":
			return SubGargoyle()

class SubCastleGhost:
	message = """you walk through the door slowly and carefully… you hear a noise and look around… dark figure emerges from the shadows…"""
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
	message = """You push the door open and walk in… you hear something behind you… you see a figure moving towards you… it’s a pale ghost screaming and reaching for you… you run away… """
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "fight":
			return SubGargoyleFight()
		elif action == "run away":
			return SubGargoyleRun()
			
class SubGargoyleRun:
	message = """Shuffle the Cards and Show me"""
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
	message = """You manage to run away… you run through a door.. And manage to jump through a window and land in the garden…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMaze()
			
class SubGargoyleRunFail:
	message = """you run away… and jump over a ladder and see a dark figure… you come closer and notice that it is a large gargoyle… will you fight or run away…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubGargoyleFight()
			
class SubGargoyleRunEpicFail:
	message = """You run away… you hear a scream and look  over your shoulder… suddenly  you run out of ground and fall off the roof…. And die.."""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubGargoyleRunEpicFail()

class SubGargoyleFight:
	message = """Shuffle cards"""
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
	message = """You enter the kitchen slowly and carefully…. You look around… you see… food and drink on the table… would you eat… or would you drink… """
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "eat":
			return SubKitchenFood()
		elif action == "drink":
			return SubKitchenDrink()

class SubKitchenFood:
	message = """You eat the delicious food… it is very tasty… after few minutes you feel different… suddenly you start coughing blood… you realise you have been poisoned… you die… """
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubKitchenFood()	

			
class SubWitchLair:
	message = """You  open the cellar door and climb down the stairs slowly and carefully… you see some one muttering over a fire… it is an old woman with white hair wearing rags…. Suddenly you realise she is a witch…. you also noticed there is a large gem stone on a shelf…
You can go back without the witch seeing you… or you can steal the gem stone… what are you going to do… go back … or steal the gem.."""
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
	message = """you walk around the castle… you reach a hedge and walk through an opening… you look around and notice that you have arrived in a garden… you start to walk among the trees you come to a cross road… one road leads to the garden other leads to the cemetery…. Which one will you take…. Cemetery or… the garden…"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "flowers":
			return SubFlowers()
		elif action == "cemetry":
			return SubCemetry()


class subTown:
