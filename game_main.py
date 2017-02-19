# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""


from GameEngine import GameEngine

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser
from random import random
from random import randint

NAO_IP = "192.168.1.110"


# Global variable to store the SpeachRec module instance
SpeachRec = None

class SpeachRecModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """

    lastWord = ''
    lastTouch = []
    
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        self.atts = ALProxy("ALAnimatedSpeech")
        self.motion = ALProxy("ALMotion") 
        self.posture = ALProxy("ALRobotPosture")
        self.touch = ALProxy("ALTouch")
        self.tts.setVolume(0.6)

        self.asr = ALProxy("ALSpeechRecognition")

        # Subscribe to the FaceDetected event:
        global memory
        self.memory = ALProxy("ALMemory")
        self.memory.subscribeToEvent("WordRecognized",
            "SpeachRec",
            "onSpeechDetected")

    def onSpeechDetected(self, eventName, value, subscriberIdentifier):
        """ This will be called each time a face is
        detected.

        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        self.memory.unsubscribeToEvent("WordRecognized",
            "SpeachRec")

        if value[1] > 0.25:
            self.lastWord = value[0]
        

        # Subscribe again to the event
        self.memory.subscribeToEvent("WordRecognized",
            "SpeachRec",
            "onSpeechDetected")

def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    # Warning: SpeachRec must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global SpeachRec
    SpeachRec = SpeachRecModule("SpeachRec")

    #setup game
    isVictory = False
    isDefeat = False
        
    g = GameEngine()

    SpeachRec.motion.wakeUp()
    configuration = {"bodyLanguageMode":"contextual"}
    time.sleep(3)
    SpeachRec.atts.say("Hello, I am Nao... Do you wan't to play a game?", configuration)

    raw_input('Yes or no')

    try:
        while (not isDefeat and not isVictory):
            msg = g.getNextMessage()
            action = g.getStateAction()
            
##            #DEBUG MESSAGE
##            print("Scenario is: "+ g.game_state)
##            print("Action is: " +action)
##            print(g.scenario.game_state)
##            print(msg)
            
            SpeachRec.atts.say(msg,configuration)
            
            if action == "combat":
                SpeachRec.tts.say('Touch me .. to influence combat..')
                time.sleep(2)
                print(SpeachRec.lastTouch)
                next_state = 100*random()
                if next_state < 20:
                    next_state = "great success"    
                elif next_state < 70:
                    next_state = "success"
                elif next_state < 90:
                    next_state = "fail"
                else:
                    next_state = "epic fail"
                    
                    
            elif action == "choice":
                g.scenario.game_state.vocabulary
                SpeachRec.asr.pause(True)
                vocabulary = g.scenario.game_state.vocabulary

                SpeachRec.atts.say('Your options are:...')
                SpeachRec.atts.say('....'.join(vocabulary))
                
                SpeachRec.asr.setVocabulary(vocabulary, False)
                SpeachRec.asr.pause(False)
                SpeachRec.lastWord = ''

                SpeachRec.asr.subscribe('Test_ASR')
                while SpeachRec.lastWord == '':
                    time.sleep(0.2)
                SpeachRec.asr.unsubscribe('Test_ASR')

                print('You Said: ' + str(SpeachRec.lastWord))
                next_state = SpeachRec.lastWord
                
            elif action == "SuccessRoll":
                next_state = random()
                print('RNGsus decides for a: '+str(next_state))
            elif action == "none":
                    next_state = 0
                     
            else:
                    raise Exception("Wrong Action.")
                    
            g.nextState(next_state)
            
            isVictory = g.isVictory()
            isDefeat = g.isDefeat()
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"

        SpeachRec.memory.unsubscribeToEvent("TouchChanged",
            "HumanGreeter")
        SpeachRec.memory.unsubscribeToEvent("WordRecognized",
            "SpeachRec")
        SpeachRec.asr.setAudioExpression(False)
        myBroker.shutdown()
        sys.exit(0)

    if isVictory:
                print(g.getNextMessage())
                SpeachRec.atts.say(g.getNextMessage())
                print("Concrats You Win!!")
                SpeachRec.tts.say('Congrats You Win!.. Badass')
    else:
                print(g.getNextMessage())
                SpeachRec.atts.say(g.getNextMessage())
                print("You Lose!")
                SpeachRec.tts.say('You Lose!')



if __name__ == "__main__":
    main()
