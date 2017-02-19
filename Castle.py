class Castle:
    def __init__(self):
        self.game_state = SubCastle()
    
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
        
class SubCastle:
    message = """You have taken the path to the castle.. you come to a stop at the gate.. you can either enter the castle.. or go round and walk through the garden.. would you enter... Or go to the garden.."""
    action = "choice"
    vocabulary = ['inside', 'garden']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "inside":
            return SubInside()
        elif action == "garden":
            return SubGarden()

class SubInside:
    message = """you push open the door.. it slowly opens in.. you walk inside.. it seems that someone was living in the castle.. you look around.. when you look up you see a staircase leading up to another floor.. you look around and see what looks like the kitchen.. also. You see another trap door leading to what looks like the cellar.. where will you go.. upstairs.. kitchen.. or.. cellar.."""
    action = "choice"
    vocabulary = ['upstairs', 'door', 'downstairs']
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
    message = """you climb the staircase slowl... you are careful not to make any noise.. you see two doors.. which one would you take.. left door or right.. """
    action = "choice"
    vocabulary = ['right', 'left']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "right":
            return SubCastleGhost()
        elif action == "left":
            return SubGargoyle()

class SubCastleGhost:
    message = """you walk through the door slowly and carefull... you hear a noise and look around.. dark figure emerges from the shadows.."""
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
    message = """You push the door open and walk in.. you hear something behind you.. you see a figure moving towards you.. it's a pale ghost screaming and reaching for you.. you run awa... """
    action = "choice"
    vocabulary = ['fight', 'run away']
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
        if action < 0.50:
            return SubGargoyleEscape()
        elif action < 0.75:
            return SubGargoyleRunFail()
        else:
            return SubGargoyleRunEpicFail()
            
class SubGargoyleEscape:
    message = """You manage to run awa... you run through a door.. And manage to jump through a window and land in the garden.."""
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubMaze()
            
class SubGargoyleRunFail:
    message = """you run awa... and jump over a ladder and see a dark figure.. you come closer and notice that it is a large gargoyle.. will you fight or run awa..."""
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubGargoyleFight()
            
class SubGargoyleRunEpicFail:
    message = """You run awa... you hear a scream and look  over your shoulder.. suddenly  you run out of ground and fall off the roof... And die.."""
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
    message = """You enter the kitchen slowly and carefull.... You look around.. you see.. food and drink on the table.. would you eat.. or would you drink.. """
    action = "choice"
    vocabulary = ['eat', 'drink']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "eat":
            return SubKitchenFood()
        elif action == "drink":
            return SubKitchenDrink()

class SubKitchenFood:
    message = """You eat the delicious food.. it is very tast... after few minutes you feel different.. suddenly you start coughing blood.. you realise you have been poisoned.. you die.. """
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubKitchenFood()

class SubKitchenDrink:
    message = "You try the trink. It tastes strange."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action < 0.5:
                return SubKitchenDrinkSuccess()
        else:
                return SubKitchenDrinkFail()

class SubKitchenDrinkFail:
    message = "The drink causes you endless hallucination. You die!"
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubKitchenDrinkFail()

class SubKitchenDrinkSuccess:
    message = "You feel refreshed and exit the castle ruins."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitInside()  
            
class SubWitchLair:
    message = """You  open the cellar door and climb down the stairs slowly and carefull... you see some one muttering over a fire.. it is an old woman with white hair wearing rags... Suddenly you realise she is a witch... you also noticed there is a large gem stone on a shelf..
You can go back without the witch seeing you.. or you can steal the gem stone.. what are you going to do.. go back .. or steal the gem.."""
    action = "choice"
    vocabulary = ['fight', 'steal', 'retreat']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "steal":
            return SubWitchSteal()
        elif action == "fight":
            return SubWitchCombat()
        elif action == "retreat":
            return SubWitchLeave()

class SubWitchLeave:
    message = """you walk around the castle.. you reach a hedge and walk through an opening.. you look around and notice that you have arrived in a garden.. you start to walk among the trees you come to a cross road.. one road leads to the garden other leads to the cemeter.... Which one will you take... Cemetery or.. the garden.."""
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubInside()

class SubWitchSteal:
    message = "You try to steal a potion from the witch."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action > 0.5:
                return SubKitchenDrink()
        else:
                return SubWitchFight()

class SubWitchFight:
    message = "The witch notices you and wants to fight."
    action = "choice"
    vocabulary = ['fight', 'run']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "run":
            return SubWitchRun()
        elif action == "fight":
            return SubWitchCombat()

class SubWitchRun:
    message = "The witch notices you and wants to fight."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action < 0.8:
                return SubWitchRun()
        else:
                return SubWitchRunFail()

class SubWitchRun:
    message = "You manage to run away from the witch, but get lost in a maze"
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubMaze()

class SubWitchRun:
    message = "You find yourself unable to escape."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubWitchCombat()

class SubWitchCombat:
    message = "You engage in combat with a wicked witch."
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
            return SubWitchFightWin()
        elif self.hp <= 0:
            return SubWitchFightLose()
        elif self.hp == 3:
            self.message = "Very Healthy"
        elif self.hp == 2:
            self.message = "Small wound"
        elif self.hp == 1:
            self.message = "Heavily wounded"
        
        return self

class SubWitchFightWin:
    message = "You defeat the witch and obtain a stylish witch hat."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitInside()
    
class SubWitchFightLose:
    message = "The witch turns you into a pig."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubWitchFightLose() 

class SubExitInside:
    message = "You walk outside and follow the road."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubFollowRoad()  

class SubGarden:
    message = "You are in the garden. Move through flowers or towards cemetry?"
    action = "choice"
    isVictory = False
    isDefeat = False
    vocabulary = ['flowers','cemetry']
    def nextState(self, action):
        if action == "flowers":
            return SubFlowers()
        elif action == "cemetry":
            return SubCemetry()

class SubFlowers:
    message = "You find a child trapped in thorns. Help or ignore?"
    action = "choice"
    vocabulary = ['help','ignore']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "help":
            return SubHelpChild()
        elif action == "ignore":
            return SubIgnoreChild()

class SubIgnoreChild:
    message = "You ignore the child. However, you bump into a wolf pack. Run or fight?"
    action = "choice"
    vocabulary = ['fight','run']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "fight":
            return SubWolfFight()
        elif action == "run":
            return SubWolfRun()

class SubWolfFight:
    message = "You engage in combat with a wolf pack."
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
            return SubWolfFightWin()
        elif self.hp <= 0:
            return SubWolfFightLose()
        elif self.hp == 3:
            self.message = "Very Healthy"
        elif self.hp == 2:
            self.message = "Small wound"
        elif self.hp == 1:
            self.message = "Heavily wounded"
        
        return self

class SubWolfFightWin:
    message = "You defeat the Wolfpack and continue your journey."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitGarden()

class SubWolfFightLose:
    message = "You end up as dinner."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubWolfFightLose()

class SubWolfRun:
    message = "You try to run away from the wolfs"
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action < 0.25:
                return SubWolfRunEpicFail()
        elif action < 0.50:
                return SubWolfRunFail()
        else:
                return SubWolfRunSuccess()

class SubMaze:
    message = "You are trapped in a maze. Only Luck will get you out."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action < 0.3:
                return SubMazeStarve()
        else:
                return SubMazeEscape()

class SubMazeStarve:
    message = "You starve while finding your way out."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubMazeStarve()

class SubMazeEscape:
    message = "You manage to escape barely and continue zour journey along the road."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubFollowRoad()

class SubWolfRunFail:
    message = "You can't outrun the wolfs and have to fight."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubWolfFight()

class SubWolfRunSuccess:
    message = "You escape the wolfs but are now trapped in a maze."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubMaze()

class SubWolfRunEpicFail:
    message = "You trip and get eaten by wolfs."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubWolfRunEpicFail()

class SubHelpChild:
    message = "You try to help the child."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action < 0.33:
           return SubHelpChildSuccess()
        elif action < 0.66:
                return SubHelpChildFail()
        else:
                return SubHelpCriticalFail()

class SubHelpChildSuccess:
    message = "You rescue the child and it runs away. You continue and exit the garden."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitGarden()

class SubHelpChildFail:
    message = "The child dies as you try to save it. You exit the garden"
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitGarden()
        
class SubHelpCriticalFail:
    message = "You fail miserably and trap yourself in the thorns."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubHelpCriticalFail

class SubCemetry:
    message = "You encounter a scarry looking ghost. Run away or engage?"
    action = "choice"
    isVictory = False
    isDefeat = False
    vocabulary = ['run','engage']
    def nextState(self, action):
        if action == "engage":
            return SubGardenGhostEngage()
        elif action == "run":
            return SubGardenGhostRun()

class SubGardenGhostEngage:
    message = "The ghost tells you a riddle. Answer coffin."
    action = "choice"
    vocabulary = ['coffin', 'chair', 'time', 'riddle']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == 'coffin':
            return SubGardenGhostSuccess()
        else:
            return SubGardenGhostDead()

class SubGardenGhostSuccess:
    message = "The ghost is satisfied and escorts you."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitGarden()

class SubExitGarden:
    message = "You exit the garden and follow the road."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubFollowRoad()

class SubGardenGhostRun:
    message = "You try to run away from the ghost."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action > 0.5:
            return SubFlowers()
        else:
            return SubGardenGhostDead()

class SubGardenGhostDead:
    message = "The ghost causes you to fall into madness."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubGardenGhostDead()

class SubFollowRoad:
    message = "You are on a road splot. Left or right?"
    action = "choice"
    vocabulary = ['left','right']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "left":
            return SubFollowRoadLeft()
        elif action == "right":
            return SubFollowRoadRight()

class SubFollowRoadLeft:
    message = "You see a beautiful landside."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubSolider()

class SubFollowRoadRight:
    message = "You see a beautiful sunset."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubSolider()

class SubSolider:
    message = "A soldider  tasks you with an important mission. Go to Manison"
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubTown()

class SubTown:
    message = "You go into the town"
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return subTown()
