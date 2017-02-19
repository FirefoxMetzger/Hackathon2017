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
    message = """You have taken the path to the castle... you come to a stop at the gate... you can either enter the castle... or go round and walk through the garden... would you enter... Or go to the garden..."""
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
    message = """you push open the door... it slowly opens in... you walk inside... it seems that someone was living in the castle... you look around... when you look up. you see a staircase leading up to another floor... you look around and see what looks like the kitchen... finally, You see another trap door leading to what looks like the cellar... where will you go... upstairs... kitchen... or.. downstairs to the celler..."""
    action = "choice"
    vocabulary = ['upstairs', 'kitchen', 'downstairs']
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action == "upstairs":
            return SubHallway()
        elif action == "kitchen":
            return SubKitchen()
        elif action == "downstairs":
            return SubWitchLair()
    
class SubHallway:
    message = """you climb the staircase slowly... you are careful not to make any noise... you see two doors... which one would you take.. left door ... right.. """
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
    message = """you walk through the door slowly and carefull... you hear a noise and look around... a dark figure emerges from the shadows..."""
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action < 0.5:
            return SubTripAndDie()
        else:
            return SubGargoyle()
            
class SubTripAndDie:
    message = """You run away... you hear a scream and look  over your shoulder... suddenly  you run out of ground and fall off the roof... And die... """
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubTripAndDie()
            
class SubGargoyle:
    message = """You push the door open and walk in... you hear something behind you... you see a figure moving towards you... it's a pale ghost screaming and reaching for you... you run away... """
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
    message = """You manage to run away... you run through a door.. And manage to jump through a window and land in the garden.."""
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubMaze()
            
class SubGargoyleRunFail:
    message = """you run awa... and jump over a ladder and see a dark figure.. you come closer and notice that it is a large gargoyle.. will you fight or run away..."""
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
    message = "looks like you would have to fight the gargoyle after all... touch my body to fight.."
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
            self.message = "You manage to run away... you run through a door... And manage to jump through a window and land in the garden..."
        elif self.hp == 2:
            self.message = "Small wound"
        elif self.hp == 1:
            self.message = "You pull your sword out to fight... the gargoyle pulls a big broadsword made out  black steel... you start to run... but you slip on the banana peel and fall and impale yourself on your own sword... you die..."
        
        return self

class SubGargoyleFightWin:
    message = "The gargoyle is coming towards you... you know you cannot fight him... so you shout... what's that... and point over the gargoyles shoulder... when it turns around to look.. you run through a door.. And manage to jump through a window and land in the garden..."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitInside()  

class SubGargoyleFightLose:
    message = "You run away... you hear a scream and look  over your shoulder... suddenly  you run out of ground and fall off the roof.... And die.."
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
    message = "you walk around the castle... you reach a hedge and walk through an opening... you look around and notice that you have arrived in a garden... you start to walk among the trees you come to a cross road... one road leads to the garden other leads to the cemetery.... Which one will you take.... Cemetery or... the garden..."
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
    message = "You go in to the garden.... all of a sudden you notice a child trapped in a thorn bush... the child seems like he was there for some time and is in a bad state... you can ignore the child.... Or Help the child...What will you do... Ignore... or Help..."
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
    message = "You ignore the child and walk away... after several minutes you hear a growl.... When you turn around there is a massive wolf... the wolf is growling and is ready to pounce.... Will you fight the wolf or wold you run away..."
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
    message = "touch my body to fight with the wolf"
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
            self.message = "As soon as the wolf jump. You jump on to a nearby tree... and from there jump on the wolfs back and stab it trough the brain... the wolf is dead... you are okay and walk towards the opening... "
        elif self.hp == 2:
            self.message = "You jump out of the way while swinging your sword... you land a blow... but it is not hard enough... the beast is just wounded....."
        elif self.hp == 1:
            self.message = "You jump out of the way while swinging your sword... you land on your own sword and manage to cut off your own hand.... You die..... due to blood loss..."
        
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
    message = "You run away... you manage to run hard and fast.. and when you look back the wolf is not following you... unfortunately after several turns. You realise you are in a maze..."
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
    message = "touch my body to escape from the maze"
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
    message = "You manage to escape barely and continue your journey along the road."
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
    message = "You feel bad for the child... I mean.. it was stupid for a child to walk to a ruined castle alone... his parents must be really irresponsible.... Anyway.. you decide to try and save the child... touch my body to save the child."
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
    message = " You use your mighty sword to cut the thorn bush and save the child.... The child is happy... he walks you to the exit of the garden..."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitGarden()

class SubHelpChildFail:
    message = "You use your sword to cut the thorn bush.... But it feels like it might be too dangerous.... So you grab his hands and pull him out.... When he is out you notice that it is too late... when you pulled the child out the thorns had torn his side.... I'm sorry but he dies... but with his dying breath he tells you how to get out of the garden...."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubExitGarden()
        
class SubHelpCriticalFail:
    message = "You are pulling the child out... suddenly a thorn pokes you in the eye.... You start screaming and blindly run around.... You fall into a nearby well.... And die..."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubHelpCriticalFail

class SubCemetry:
    message = "You walk towards the cemetery.... You look around ... it is gloomy and foreboding.... Lot of old trees and gravestones lay about.... You notice the gate to exit the cemetery on the other side of the graveyard... you start walking towards it through the gravestones.... Suddenly a howling wind blows and it becomes very cold.... A ghostly figure appear s before you... would you run... or engage"
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
    message = "The ghost says ... Who makes it... has no need of it..... who buys it... has no use for it.... Who.. uses it... can neither see.. nor feel it.... I have one as well.... Answer this riddle and I... will let you pass.. or else..."
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
    message = "The ghost is satisfied... and he disappears and the path becomes clear...you walk to the gate and exit the graveyard... "
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubFollowRoad()

class SubGardenGhostRun:
    message = "You try... to run away from the ghost... touch my body to see what happed next..."
    action = "SuccessRoll"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        if action > 0.5:
            return SubFlowers()
        else:
            return SubGardenGhostDead()

class SubGardenGhostDead:
    message = "The ghost curses you... and you start to run across the graveyard... suddenly you trip over a grave and hit your head on a grave stone... and you die..."
    action = "none"
    isVictory = False
    isDefeat = True
    def nextState(self, action):
        return SubGardenGhostDead()

class SubFollowRoad:
    message = "you are on the cross roads... Left... or right?"
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
    message = "You see a beautiful landscape... it reminds you the stories you heard about valhalla..."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubSolider()

class SubFollowRoadRight:
    message = "You see a beautiful sunset... it is so beautiful. it makes you cry..."
    action = "none"
    isVictory = False
    isDefeat = False
    def nextState(self, action):
        return SubSolider()

class SubSolider:
    message = "after some hours you meat a soldier... the soldier ask you a riddle.... you are tired and wounded... you have no time for riddles... you slap the idiot couple of times.. and get the information you need... finaly you know your goal is in the nearby town..."
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
