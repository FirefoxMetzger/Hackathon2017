class Forest:
	def __init__(self):
		self.game_state = SubForest()
	
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
			return "Forest"
		
	def isVictory(self):
		return self.game_state.isVictory
	
	def isDefeat(self):	
		return self.game_state.isDefeat
		
class SubForest:
	message = """You walk in to the forest… it looks dark… ancient trees grow 
				in there… you feel as if they are looking down at you… will you 
				enter the forest or... walk along the forest."""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "into forest":
			return SubSpider()
		elif action == "border":
			return SubCamp()	

class SubSpider:
	message = """you are walking deep in to the forest… you hear a noise... 
				you look around… there is a massive spider waiting to attack 
				you. Will you fight it… Or will you run away…"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "fight":
			return SubSpiderFight()
		elif action == "flight":
			return SubSpiderFlight()
			
class SubSpiderFlight:
	message = """shuffle your cards and show me please""" 
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.33:
			return SubSpiderRunFail()
		elif action < 0.66:
			return SubLostInWoods()
		else:
			return SubSpiderForceFight()

class SubSpiderForceFight:
	message = "The Spider is to fast. You have to fight"
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSpiderFight()	
		
class SubSpiderRunFail:
	message = """But you slip on a banana peel. And fall on your face… 
				when you turn around the spider is almost upon you… you 
				are forced to fight…"""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubSpiderRunFail()
		
class SubSpiderFight():
	message = """shuffle your cards and show me please"""
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
			return SubSpiderWin()
		elif self.hp <= 0:
			return SubSpiderDie()
		elif self.hp == 3:
			self.message = "Very Healthy"
		elif self.hp == 2:
			self.message = "Small wound"
		elif self.hp == 1:
			self.message = "Heavily wounded"
		
		return self
			
class SubSpiderWin:
	message = """YES… you managed a critical hit and Spider is Dead…  you walk 
				past it’s body. After several hours you stumble upon a road… 
				you are releaved…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()
		
class SubSpiderDie:
	message = """I am so sorry but the spider manage to sting you… you die… slowly…"""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubSpiderRunFail()
			
			
class SubCamp:
	message = """You are walking along the border of the forest and you come upon a campfire… there is a bore roasting over the fire… there is a tent… and you notice a chest… you are interested in the chest… Would you wait for the owners to come back….. or.. eat the bore…. Or Try to open the chest…. Choose wisely…."""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "wait":
			return SubCampWait()
		elif action == "eat":
			return SubCampEat()
		elif action == "steal":
			return SubCampLock()
			
class SubCampWait:
	message = """The people turn out to be robbers… and they are not happy to see you… Now you have to fight them…."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
		
class SubCampEat:
	message = """You eat the bore… you feel sleepy and fall asleep… when you wake up the owners have arrıved to the camp and they are band of thieves.  Now you have to fıght them to death…."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()

class SubCampLock:
	message = """You try to pıck the lock for several mınutes wıthout success… then you try to break open the box… when you manage to open ıt… you fınd out that ıt ıs empty… you hear a sound… when you look around you see the owners of the camp has returned… they are robbers and they are angry… you have to fıght them…"""
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.33:
			return SubCampLockOpen()
		elif action < 0.66:
			return SubCampLockBreak()
		else:
			return SubCampLockFail()

class SubCampLockOpen:
	message = "You open the chest. It is empty. You turn around and see a bandit."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
			
class SubCampLockBreak:
	message = "Your break the chest while you try to brutally open it and destroy the content. You turn around and see a bandit."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
			
class SubCampLockFail:
	message = "You're lockpick breaks while you try and open the chest. You turn around and see a bandit."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
		
class SubBandit:
	message = "Fierce looking bandit. Fight or flight?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "flight":
			return SubBanditFlight()
		elif action == "fight":
			return SubBanditFight()
			
class SubBanditFlight:
	message = "You try and run away from the bandit."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action > 0.5:
			return SubBanditFight()
		else:
			return SubLostInWoods()
			
class SubLostInWoods:
	message = "You escabe, but are now lost in the woods."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.33:
			return SubSign()
		elif action < 0.66:
			return SubScreams()
		else:
			return SubRobbers()
			
class SubSign:
	message = "You stumble into a sign, that shows you the way."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()
		
class SubRobbers:
	message = "You stumble into robbers that kill you."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubRoad()
		
class SubScreams:
	message = "You are lost, but you hear screams. Follow them?"
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "follow":
			return SubForestWitch()
		elif action == "ignore":
			return SubSwamp()
			
class SubForestWitch:
	message = "It was a witch, you die."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubForestWitch()
			
class SubSwamp:
	message = "You are lost, but you hear screams. Follow them?"
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.33:
			return SubSwampMonster()
		elif action < 0.66:
			return SubSwampSink()
		else:
			return SubSwampSurvive()

class SubSwampSink:
	message = "You sink into a pit and die."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubRoad()
		
class SubSwampMonster:
	message = "Swamp monster bites your head off."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubRoad()

class SubSwampSurvive:
	message = "You magically survive the swamp and find a road that you follow."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()

class SubBanditFight():
	message = "You fight the bandit."
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
			return SubBanditWin()
		elif self.hp <= 0:
			return SubBanditDie()
		elif self.hp == 3:
			self.message = "Very Healthy"
		elif self.hp == 2:
			self.message = "Small wound"
		elif self.hp == 1:
			self.message = "Heavily wounded"
		
		return self
		
class SubBanditWin:
	message = "You Kill the bandit and continue to walk along the road."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()
		
class SubBanditDie:
	message = "You die while fighting the bandit."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubBanditDie()
		
class SubRoad:
	message = """ you walk along the road and reach a cross road… will you go left… or right… """
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "right":
			return SubSolider()
		elif action == "left":
			return SubMerchant()
			
class SubMerchant:
	message = """you take the left path and start walking… after some time. 
				You hear something close in front of you… It is a merchant 
				who seem to be very wealthy… you can either rob and steal 
				his goods or ask him for his help… """
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "steal":
			return SubMerchantRob()
		elif action == "ask":
			return SubMerchantAsk()
			
class SubMerchantRob:
	message = """You sneak up behind him and ambush him… Shuffle your cards and show me… lets see if you succeeded or not…"""
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.6:
			return SubMerchantRobSuccess()
		else:
			return SubMerchantRobFail()
			
class SubMerchantRobSuccess:
	message = """you managed to successfully subdue the merchant… 
				He has a large amount of money …"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSolider()
		
class SubMerchantRobFail:
	message = """you find out merchants dark secret… he is a slaver… 
				he takes you captive as a slave… """
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMerchantRobFail()
			
class SubMerchantAsk:
	message = """you learn a dark secret about the merchant… he is a slaver… 
				he has a large number of slaves in his wagon… you are obligated 
				to free the slaves…"""
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "free":
			return SubMerchantAskFree()
		elif action == "ignore":
			return SubMerchantAskIgnore()
			
class SubMerchantAskFree:
	message = """Lets see if you can free the slaves… shuffle the cards and 
				pick one... and show it to me…"""
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action <= 0.6:
			return SubMerchantAskFreeSuccess()
		else:
			return SubMerchantRobFail()
		
class SubMerchantAskFreeSuccess:
	message = """You free the slaves … you bound the slaver… one of the slaves 
				turn out to be a soldier… he tells you to go to a nearby town 
				where the town people needs you…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSolider()
			
class SubMerchantAskIgnore:
	message = "You ignore the slaves, leave the merchant behind and move on."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSolider()
			
class SubSolider:
	message = """You take the right path… after some hours you meat a soldier… the soldier tells you that you are needed in to the small town that lies ahead…"""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubTown()
		
class SubTown():
	message = "Thus, you decide to walk into the town."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubTown()
