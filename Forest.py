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
	message = "You arrive at the forest border. Walk into forest or along boder?"
        vocabulary = ['into forest','border']
	action = "choice"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "into forest":
			return SubSpider()
		elif action == "border":
			return SubCamp()	

class SubSpider:
	message = "You bump into a spider."
	action = "choice"
	vocabulary = ['fight','flight']
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "fight":
			return SubSpiderFight()
		elif action == "flight":
			return SubSpiderFlight()
			
class SubSpiderFlight:
	message = "You try to run away from the spider."
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
	message = "You try to run, but you trip and die."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubSpiderRunFail()
		
class SubSpiderFight():
	message = "You fight the spider."
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
	message = "You kill the spider, but find nothing of use. You continue along the road."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()
		
class SubSpiderDie:
	message = "You die while fighting the Spider."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubSpiderRunFail()
			
			
class SubCamp:
	message = "You see a campfire."
	action = "choice"
	vocabulary = ['wait','eat','steal']
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
	message = "You wait until the person comes back. He is a bandit."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
		
class SubCampEat:
	message = "You eat, need to sleep. Walke up find bandit."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()

class SubCampLock:
	message = "You try to pick the lock. Let's see how you are doing."
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
	vocabulary = ['flight','fight']
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
	vocabulary = ['follow','ignore']
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
	message = "You come to a road split. Go left or right?"
	action = "choice"
	vocabulary = ['right','left']
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "right":
			return SubSolider()
		elif action == "left":
			return SubMerchant()
			
class SubMerchant:
	message = "You see a merchant. He didn't notie you. Steal or ask for trade?"
	action = "choice"
	vocabulary = ['steal','ask']
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "steal":
			return SubMerchantRob()
		elif action == "ask":
			return SubMerchantAsk()
			
class SubMerchantRob:
	message = "You try to rob the merchant."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.6:
			return SubMerchantRobSuccess()
		else:
			return SubMerchantRobFail()
			
class SubMerchantRobSuccess:
	message = "You rob the Merchant, get some money, and run along."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSolider()
		
class SubMerchantRobFail:
	message = "The Merchant notices, calls his friends. You are now a slave as well."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMerchantRobFail()
			
class SubMerchantAsk:
	message = "You engage the merchant. He is a slave trader. Free slaves or ignore?"
	action = "choice"
	vocabulary = ['free','ignore']
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "free":
			return SubMerchantAskFree()
		elif action == "ignore":
			return SubMerchantAskIgnore()
			
class SubMerchantAskFree:
	message = "You try to free the slaves."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action <= 0.6:
			return SubMerchantAskFreeSuccess()
		else:
			return SubMerchantRobFail()
		
class SubMerchantAskFreeSuccess:
	message = "You free the slaves and they run away. You continue along the road."
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
	message = "You find a Solider. You have to go into town and molest the elder's daughter."
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
