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
		return "Town"
		
	def isVictory(self):
		return self.game_state.isVictory
	
	def isDefeat(self):	
		return self.game_state.isDefeat

class SubTown:
	message = "Town Message"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "Manson":
			return SubManson()
		elif action == "Armory":
			return SubArmory()
		elif action == "Alchemist":
			return SubAlchemist()

class SubManson:
	message = "Manson Message"
	action = "choice"
	isVictory = False
	isDefeat = False
		
	def nextState(self, action):
		if action == "break in":
			print("test")
			return SuccessRollManson()
		elif action == "talk_guard":
			return SubTown()
		elif action == "fight":
			return subMansonFight()
			
class SuccessRollManson:
	message = "Roll Dice"
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
		
	def nextState(self, action):
		if action > 0.5:
			return SubMansonGuards()
		else:
			return SubMansonDie()
			
class SubMansonDie:
	message = "You break your legs and die"
	action = "choice"
	isVictory = False
	isDefeat = True
		
	def nextState(self, action):
		pass
		
class SubMansonGuards:
	message = "You climb over fence, but guards inside spot you. You go to jail."
	action = "none"
	isVictory = False
	isDefeat = False
		
	def nextState(self, action):
		return SubJail()
		
class SubJail:
	message = "You are in Jail. You miss your adventure."
	action = "none"
	isVictory = False
	isDefeat = True
		
	def nextState(self, action):
		return SubJail()	
		
class subMansonFight:
	message = "Fight Guards in front of Manson"
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
			return WinSubMansonFight()
		elif self.hp <= 0:
			return DieSubMansonFight()
		elif self.hp == 3:
			self.message = "Very Healthy"
		elif self.hp == 2:
			self.message = "Small wound"
		elif self.hp == 1:
			self.message = "Heavily wounded"
		
		return self
		
class WinSubMansonFight:
	message = "You smash guards. Call reinforcement you go to jail"
	action = "choice"
	isVictory = False
	isDefeat = True

class DieSubMansonFight:
	message = "You die fighting the Guards in front of the Manson."
	action = "choice"
	isVictory = False
	isDefeat = True
	
class SubArmory:
	message = "Armory Message"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "ask guard":
			return SubArmoryToTown()
		elif action == "break in":
			# NEED TO DEFINE CHANCE CLASS
			return SubArmoryBreakIn()
			
class SubArmoryToTown:
	message = "You talk to guard. Get Lost. Back to town."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubTown()
		
class SubArmoryBreakIn:
	message = "Breaking into Armory"
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action > 0.3:
			return SubArmoryBreakInSuccess()
		else:
			return SubArmoryBreakInFail()
			
class SubArmoryBreakInFail:
	message = "You are spotted and imprisoned by guards."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubJail()
		
class SubArmoryBreakInSuccess():
	message = "Succeed breaking into armory. Steal what?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "shield":
			return SubArmoryStealShield()
		elif action == "armor":
			return SubArmoryStealArmor()
		elif action == "locked chest":
			return SubArmoryLockedChest()

class SubArmoryStealShield():
	message = "You Steal the shield and continue to enter the manson."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMansonWithArmor()
			
class SubArmoryStealArmor():
	message = "You Steal the shield and continue to enter the manson."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMansonWithArmor()
		
class SubArmoryLockedChest():
	message = "While you try to lockpick the chest, a group of guards show up. They imprison you."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubJail()
			
class SubMansonWithArmor():
	message = "At Manson With armor."
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "intimidate":
			return SubMansonArmorIntimidate()
		elif action == "fight":
			return SubMansonArmorFight()
			
class SubMansonArmorIntimidate():
	message = "You try to intimidate the guards."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action >= 0.4:
			return SubMansonArmorToLeader()
		else:
			return SubMansonArmorFight()
			
class SubMansonArmorToLeader():
	message = "The scared guards escort you to their leader."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubInManson()
		
class SubInManson():
	message = "You encounter the village elder and marry his beautiful daughter."
	action = "none"
	isVictory = True
	isDefeat = False
	def nextState(self, action):
		return SubInManson()
			
class SubMansonArmorFight():
	message = "You engage the guards in combat."
	action = "combat"
	isVictory = False
	isDefeat = False
	
	hp = 5
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
			return SubInManson()
		elif self.hp <= 0:
			return SubMansonArmorFightDie()
		elif self.hp >= 3:
			self.message = "Very Healthy"
		elif self.hp == 2:
			self.message = "Small wound"
		elif self.hp == 1:
			self.message = "Heavily wounded"
		
		return self
		
class SubMansonArmorFightDie:
	message = "Despite using protection you fail to win against the guards. They kill you."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMansonArmorFightDie()

			
class SubAlchemist:
	message = "Alchemist Message"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "black potion":
			return SubBlackPotion()
		elif action == "blue potion":
			# NEED TO DEFINE CHANCE CLASS
			return SubBluePotion()
		elif action == "green potion":
			# NEED TO DEFINE CHANCE CLASS
			return SubGreenPotion()
			
class SubBlackPotion:
	message = "The Black potion was poisenous. You Die."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubBlackPotion()
		
class SubBluePotion:
	message = "You feel strong, but also poisoned"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "ignore":
			return SubMansonPoisoned()
		elif action == "antidote":
			return SubPoorChild()
			
class SubMansonPoisoned:
	message = ("You decide to ignore your feeling and go to the Manson.",
	"When you arrive you can barely stand and feel like throwing up.")
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "Town":
			return SubMansonPoisonedDie()
		elif action == "talk guard":
			return SubMansonPoisonedDie()
			
class SubMansonPoisonedDie:
	message = ("You faint on your way.",
	"Ignoring poison is a bad idea. You are dead.")
	action = "choice"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMansonPoisonedDie()
			
class SubPoorChild:
	message = "You find a poor child, which happens to have the antidote."
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "steal":
			return SubPoorChildSteal()
		elif action == "ask":
			return SubPoorChildAsk()

class SubPoorChildAsk:
	message = "She woun't give you the antidote, she has to cure her grandma."
	action = "choice"
	isVictory =False
	isDefeat = False
	def nextState(self, action):
		if action == "steal":
			return SubPoorChildSteal()
		elif action == "kill":
			return SubPoorChildKill()			

class SubPoorChildSteal:
	message = "You try to steal the antidote from the girl."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action >= 0.5:
			return SubMansonStrength()
		else:
			return SubMansonPoisonedDie()		


class SubPoorChildKill:
	message = "Heartless Bastard. You have no trouble killing her and obtain the antidote."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMansonStrength()

class SubMansonStrength:
	message = "You managed to cure your poison and head for the manson."
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "jump":
			return SubMansonStrengthJump()
		elif action == "fight":
			return SubMansonArmorFight()
			
class SubMansonStrengthJump:
	message = "You try to jump over the wall using your superhuman strength."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action >= 0.2:
			return SubInManson()
		else:
			return DieStrengthMansonJump()
			
class DieStrengthMansonJump:
	message = "You jump over the wall, but land unlucky and break your legs. You die."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return DieStrengthMansonJump()
		
class SubGreenPotion:
	message = ("The green potion was delicious. You have trouble staying",
	"awake and fall into a slumber. When you wake up you are surrounded by guards.",
	"They take you to the prison")
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubJail()
