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
    message = "You are going into an ancient castle ruin. Go inside or into garden?"
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
    message = "You are inside the castle. Go upstairs, downstairs or through door?"
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
    message = "You go upstairs into the hallway. Left door or right?"
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
    vocabulary = ['eat', 'drink']
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
    message = "You find a witch lair. Fight, steal or retreat?"
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
    message = "You pussy out and go back to the hallway."
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
