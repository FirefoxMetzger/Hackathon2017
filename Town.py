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
	message = """you enter the town to look around… you talk about and ask people about the town… you hear that there are three places you are interested in going… The alchemist where you can find the portions to help you recover from your wounds… The armoury to repair your armour and sword… and the mansion where you have some personal business… where do you go to… to meet the alchemist… go to the armoury… or go to the mansion…"""
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
	message = """you go to the mansion…. You have heard a rumour.  that your long-lost love. Brunilda.. is imprisoned in the mansion… the mansion belongs to rich man and it is guarded by Spartan mercenaries….you can talk to the guards…. or You can fight your way through now… or break in later…. What will you do?.."""
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
	message = """you manage to break in at night… you are assuming all will be sleeping… will you succeed…. """
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
		
	def nextState(self, action):
		if action > 0.5:
			return SubMansonGuards()
		else:
			return SubMansonDie()
			
class SubMansonDie:
	message = """You have underestimated the security…. You get caught and the guards think you have come to molest the lady of the house… you are beaten to death… you… die…"""
	action = "choice"
	isVictory = False
	isDefeat = True
		
	def nextState(self, action):
		pass
		
class SubMansonGuards:
	message = "You manage to climb over fence, but guards inside spot you. You go to jail."
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
	message = """You manage to fight through all the guards and kill them all….. you break through door after door… you find the rich man… you hold him at sword point.. and ask him to take you to Brunilda…. Finally after a long. Long time you are together…. you take her in your arms and go to the stables…. You grab two horses and ride on. To the sunset…."""
	action = "choice"
	isVictory = False
	isDefeat = True

class DieSubMansonFight:
	message = """You jump on the soldiers roaring like a crazy person…. They point their spears upwards and you get yourself impaled on them…. You die.. like an idiot…"""
	action = "choice"
	isVictory = False
	isDefeat = True
	
class SubArmory:
	message = """You go to the armoury to find the equipment… you look around the place… you see what you are looking for …. But the equipment are expensive… would you come later and steal the equipment… or ask from the blacksmith for some free service…."""
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
	message = """you ask the black smith for some free stuff…. He looks at you and tell you to get lost… and kick you out of the armoury…."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubTown()
		
class SubArmoryBreakIn:
	message = """you manage to break in at night… you are assuming all will be sleeping… will you succeed…. """
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action > 0.3:
			return SubArmoryBreakInSuccess()
		else:
			return SubArmoryBreakInFail()
			
class SubArmoryBreakInFail:
	message = """You have underestimated the security…. You get caught and the guards think you have come to molest the lady of the house… you are beaten to death… you… die…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubJail()
		
class SubArmoryBreakInSuccess():
	message = """you go to the armoury in the middle of the night….. you break into the place and start searching the place…. you go through the expensive items… you have three options…. you can either take a shield… an armour…. Or a chest that is heavy and locked…. Which one will you take…."""
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
	message = """You manage to escape with the shield….. now you travel to the mansion…."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMansonWithArmor()
			
class SubArmoryStealArmor():
	message = """Success….. you manage to escape with the armour…..  and go to the mansion…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMansonWithArmor()
		
class SubArmoryLockedChest():
	message = """you manage to climb on to the wall with the chest… but unfortunately when you try to climb down.. you slip and fall…. The chest crushes your left knee… you are caught and sent to jail… you rot their…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubJail()
			
class SubMansonWithArmor():
	message = """you go to the mansion…. You have heard a rumour.  that your long-lost love. Brunilda.. is imprisoned in the mansion… the mansion belongs to rich man and it is guarded by Spartan mercenaries….you talk to the guards…. They tell you to get lost… You can fight your way through now… or break in later…. What will you do?.."""
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
	message = "The guards are very scared… they take you to the merchant… you hold him at sword point.. and ask him to take you to Brunilda…."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubInManson()
		
class SubInManson():
	message = """Finally after a long. Long time you are together…. you take her in your arms and go to the stables…. You grab two horses and ride on. To the sunset…."""
	action = "none"
	isVictory = True
	isDefeat = False
	def nextState(self, action):
		return SubInManson()
			
class SubMansonArmorFight():
	message = """You failed to intimidate the Spartans …. Because they are… well… Spartans… now you have to fight... """
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
	message = """You jump on the soldiers roaring like a crazy person…. They point their spears upwards and you get yourself impaled on them…. You die.. like an idiot…"""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMansonArmorFightDie()

			
class SubAlchemist:
	message = """You enter the alchemists shop… although he like to help you he proposes that you choose the portion without telling you what they are… he places three portions in front of you… one black… one blue… and one green… which one will you select…"""
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
	message = """You drink the black portion… it smells like black tar oil… suddenly your insides burn… it turns out to be poison… you fall…… and .... die…"""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubBlackPotion()
		
class SubBluePotion:
	message = """you drink the blue portion… it smells like onions and bacon…. Suddenly you feel like you have been hit by lightning…. When you wake up the alchemist informs you that the portion has given you superhuman strength but has also contains poison….  Only way for you to survive is to find the antidote"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "ignore":
			return SubMansonPoisoned()
		elif action == "antidote":
			return SubPoorChild()
			
class SubMansonPoisoned:
	message = """you laugh at the alchemist and walk away…you go to the mansion to take care of your personal business… you see a town guard… Talk to him or go to town"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "Town":
			return SubMansonPoisonedDie()
		elif action == "talk guard":
			return SubMansonPoisonedDie()
			
class SubMansonPoisonedDie:
	message = """You feel weird… cough…. Fall to the ground…. And die…."""
	action = "choice"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMansonPoisonedDie()
			
class SubPoorChild:
	message = """you heist to find the antidote… you talk to several people… try to find the antidote… finally you find a child with the correct antidote.... you can either steal the portion or… you can ask for it… what will you do…"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "steal":
			return SubPoorChildSteal()
		elif action == "ask":
			return SubPoorChildAsk()

class SubPoorChildAsk:
	message = """You ask the child for the antidote… the child refuses and tells you that it is for his grandmother…. You can either steal it… or you can kill him and take it by force…. What will you do…"""
	action = "choice"
	isVictory =False
	isDefeat = False
	def nextState(self, action):
		if action == "steal":
			return SubPoorChildSteal()
		elif action == "kill":
			return SubPoorChildKill()			

class SubPoorChildSteal:
	message = """You try to steal the antidote…"""
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action >= 0.5:
			return SubMansonStrength()
		else:
			return SubMansonPoisonedDie()		


class SubPoorChildKill:
	message = """You manage to strangle the child and take the antidote…  now you are cured… and also have super strength…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubMansonStrength()

class SubMansonStrength:
	message = """You successfully manage to steal the antidote… and now you have super strength … and also not dying…. You go to the mansion…. It is surrounded by a massive wall… at the gate there are many guards…. You can either engage the guards or… jump the wall…"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "jump":
			return SubMansonStrengthJump()
		elif action == "fight":
			return SubMansonArmorFight()
			
class SubMansonStrengthJump:
	message = """You mange to jump over the wall easily with your super strength…."""
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action >= 0.2:
			return SubInManson()
		else:
			return DieStrengthMansonJump()
			
class DieStrengthMansonJump:
	message = """You jump over a really tall wall…. When you land.. you brake your legs… guards find you get caught and the guards think you have come to molest the lady of the house… you are beaten to death… you… die…"""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return DieStrengthMansonJump()
		
class SubGreenPotion:
	message = """You drink the green portion…. It tastes like peppermint…. You fall a sleep… when you wake up you notice that you are in the jail… then you realise that the alchemist had framed you…. You rot in prison…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubJail()
