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
	message = """You walk in to the forest.. it looks dark and very old... trees that grow there are from the begining of time it self.... you have heard many stories about the dangers  of the forest...
				after some time... you feel as if some one is watching you at you... will you 
				enter the forest.... or. walk along the forest..."""
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
	message = """you are walking deep in to the forest... you hear a noise... 
				and when you turn around... there is a massive spider waiting to attack 
				you... Will you fight it... Or will you run away..."""
	action = "choice"
	vocabulary = ['fight','Run away']
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action == "fight":
			return SubSpiderFight()
		elif action == "Run away":
			return SubSpiderFlight()
			
class SubSpiderFlight:
	message = """You are battling the spider...""" 
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
	message = """you start to run... But you slip on a banana peel. And fall on your face... 
				when you turn around the spider is almost upon you... you 
				are forced to fight..."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSpiderFight()	
		
class SubSpiderRunFail:
	message = """But you slip on a banana peel. And fall on your face... 
				when you turn around the spider is almost upon you... you 
				are forced to fight..."""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubSpiderRunFail()
		
class SubSpiderFight():
	message = """Touch me if you want to fight..."""
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
			self.message = """You delivered a Hit... But the spider is not dead... but is wounded and angry..."""
		elif self.hp == 2:
			self.message = """You delivered a Hit... But the spider is not dead... but is wounded and angry..."""
		elif self.hp == 1:
			self.message = "I am so sorry... but the spider manage to sting you... you die... slowly..."
		
		return self
			
class SubSpiderWin:
	message = """YES... you managed a critical hit and Spider is Dead...  you walk 
				past it's body... After several hours you stumble upon a road... 
				you are releaved..."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()
		
class SubSpiderDie:
	message = """I am so sorry but the spider manage to sting you... you die... slowly..."""
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubSpiderRunFail()
			
			
class SubCamp:
	message = """You are walking along the border of the forest and you come upon a campfire... there is a bore roasting over the fire... there is a tent... and you notice a chest... you are interested in the chest... Would you wait for the owners to come back..... or.. eat the bore.... Or Try to open the chest.... Choose wisely...."""
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
	message = """The people turn out to be robbers... and they are not happy to see you... Now you have to fight them...."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
		
class SubCampEat:
	message = """You eat the bore... you feel sleepy and fall asleep... when you wake up the owners have arrived to the camp and they are band of thieves.  Now you have to fight them to death...."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()

class SubCampLock:
	message = """You try to pick the lock for several minutes without success... then you try to break open the box... when you manage to open it... you find out that it is empty... you hear a sound... when you look around you see the owners of the camp has returned... they are robbers and they are angry... you have to fight them..."""
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
	message = "You try to pick the lock for several minutes without success... then you try to break open the box... when you manage to open it... you find out that it is empty... you hear a sound... when you look around you see the owners of the camp has returned... they are robbers and they are angry... you have to fight them..."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
			
class SubCampLockFail:
	message = "You're lockpick breaks while you try and open the chest... You turn around and see a robber with dreadlocks and a nose ring..."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubBandit()
		
class SubBandit:
	message = "The people turn out to be robbers... and they are not happy to see you... Now you have to fight them.... or run away."
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
	message = "You try and run away from the robbers."
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action > 0.5:
			return SubBanditFight()
		else:
			return SubLostInWoods()
			
class SubLostInWoods:
	message = "You run away... but are now lost in the woods."
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
	message = "You stumble into a sign... that shows you the way... you might still be able to complete the quest"
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
	message = "you run away stumbling... but now you are lost in the forest...You keep walking without knowing where you are going... after hours and hours of walking you hear children screaming... Will you walk towards to the screams to help... or will you walk away ignoring the screams... choose wisely..."
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
	message = "You walk towards the screams... you see a child in the middle of an opening... you run towards it... a huge cage drops on your head... you realise it is a trap set by a witch... you are a slave for her to practice her magic on..."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubForestWitch()
			
class SubSwamp:
	message = "You keep walking without knowing where you are going... after hours and hours of walking you hear children screaming... Will you walk towards to the screams to help... or will you walk away ignoring the screams"
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
	message = "You keep walking away... after several miles... the path gets darker... suddenly you notice that you are sinking... too late you realise that you have stepped on quick sand... You struggle to pull away... but more you struggle. Faster you sink... within minutes you are totally submerged... die..."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubRoad()
		
class SubSwampMonster:
	message = "You are stuck in quicksand... To make matters worse... You hear a roar... when you turn around you see a massive beast... even before you manage to scream... The beast is upon you... you die... violently..."
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubRoad()

class SubSwampSurvive:
	message = "You manage to grab a hanging vine just in time... you pull yourself out... you start walking to the opposite direction and stumble upon a road..."
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubRoad()

class SubBanditFight():
	message = "You fight the bandit... manage to kill them all.."
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
			self.message = "you jump in to a tree branch and swing yourself up... you run along the branch... jump and stab the robber through the head.."
		elif self.hp == 2:
			self.message = "you swing and you miss..."
		elif self.hp == 1:
			self.message = "you swing... "
		
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
	message = """ you walk along the road and reach a cross road... will you go left... or right... """
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
	message = """you take the left path and start walking... after some time. 
				You hear something close in front of you... It is a merchant 
				who seem to be very wealthy... you can either rob and steal 
				his goods or ask him for his help... """
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
	message = """You sneak up behind him and ambush him... touch my body... lets see if you succeeded or not..."""
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action < 0.6:
			return SubMerchantRobSuccess()
		else:
			return SubMerchantRobFail()
			
class SubMerchantRobSuccess:
	message = """you managed to successfully subdue the merchant... 
				He has a large amount of money ..."""
	action = "none"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		return SubSolider()
		
class SubMerchantRobFail:
	message = """you find out merchants dark secret... he is a slaver... 
				he takes you captive as a slave... """
	action = "none"
	isVictory = False
	isDefeat = True
	def nextState(self, action):
		return SubMerchantRobFail()
			
class SubMerchantAsk:
	message = """you learn a dark secret about the merchant... he is a slaver... 
				he has a large number of slaves in his wagon... you are obligated 
				to free the slaves..."""
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
	message = """Lets see if you can free the slaves... shuffle the cards and 
				pick one... and show it to me...""" 
	action = "SuccessRoll"
	isVictory = False
	isDefeat = False
	def nextState(self, action):
		if action <= 0.6:
			return SubMerchantAskFreeSuccess()
		else:
			return SubMerchantRobFail()
		
class SubMerchantAskFreeSuccess:
	message = """You free the slaves ... you bound the slaver... one of the slaves 
				turn out to be a soldier... he tells you to go to a nearby town 
				where the town people needs you..."""
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
	message = """after some hours you meat a soldier... the soldier ask you a riddle.... you are tired and wounded... you have no time for riddles... you slap the idiot couple of times.. and get the information you need... finaly you know your goal is in the nearby town..."""
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
