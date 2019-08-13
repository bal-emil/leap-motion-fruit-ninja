#All imports and modules needed here
#-------------------------------------------------------------------------------

from UIButtonsClasses import *
from Tkinter import *
from mainClasses import *
from PIL import Image, ImageTk
from importantGameFunctions import *
import copy


#this file runs the animation frameworks and the run fucntions for each of the
#respectives modes. It calls on all the other files for their functions
#so the one file is not absurdly long.
#you must run this file to play the term project from the terimal


#____________________________MAIN ANIMATION FUNCTION____________________________
#-------------------------------------------------------------------------------




def init(data):
    
    data.mode = "homeScreen"

    data.controller = Leap.Controller() #Our main controller for the game
    data.listener = getFingerPosition(data.controller) #Listener for the Leap

    data.player = Player(data) #initiallizing the player

    data.leapYStart = 150 #these defines the interaction box above the leap 
    data.leapYEnd = 450   #in (mm)
    data.leapXStart = -150
    data.leapXEnd = 150


    data.fruit = []
    data.pieces = []
    data.gravity = 0.3
    data.paused = False
    data.gameOver = False

    data.background = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/bckgrnd.gif")
    data.water = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/water.gif")
    data.waterBit1 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/waterBit1.gif")
    data.waterBit2 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/waterBit2.gif")
    data.waterBit3 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/waterBit3.gif")
    data.waterBit4 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/waterBit4.gif")
    data.orange = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/orange.gif")
    data.orangeBit1 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/orangeBit1.gif")
    data.orangeBit2 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/orangeBit2.gif")
    data.orangeBit3 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/orangeBit3.gif")
    data.orangeBit4 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/orangeBit4.gif")
    data.coco = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/coco.gif")
    data.cocoBit1 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/cocoBit1.gif")
    data.cocoBit2 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/cocoBit2.gif")
    data.cocoBit3 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/cocoBit3.gif")
    data.cocoBit4 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/cocoBit4.gif")
    data.button1 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/button1.gif")
    data.button2 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/button2.gif")
    data.button3 = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/button3.gif")
    data.bombImage = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/bomb.gif")
    data.logo = PhotoImage(file = "/Users/EMIL/Desktop/completelyNewTP2File/logo.gif")

    pilImage = Image.open("/Users/EMIL/Desktop/completelyNewTP2File/background.jpg")
    data.backgroundImage = ImageTk.PhotoImage(pilImage)

    initHomeScreen(data)
    initAboutPage(data)
    initPlayClassic(data)
    initPlayTraining(data)
    initPlayZen(data)
    initAI(data)


    data.fruitSelect = [data.water, data.orange, data.coco]
    data.pieceSelect = {data.water: [data.waterBit1, data.waterBit2, data.waterBit3, data.waterBit4],
     data.orange: [data.orangeBit1, data.orangeBit2, data.orangeBit3, data.orangeBit4],
      data.coco: [data.cocoBit1, data.cocoBit2, data.cocoBit3, data.cocoBit4]}

    data.zenTimeTotal = 30000
    data.zenTime = 0
    data.zenTimeString = ""
    data.trainingTime = 0
    data.timer = 0
    data.level = 0
    data.showTrace = False

    data.skillTime = 0
    data.skillRating = 0
    data.previousRatings = []
    data.tempLives = 100

    data.fruitsCut = 0
    data.skillTime = 0
    data.checkTime = 0
    data.fruitsInAir = 0
    data.bombCount = 0
    data.allCutTimer = 0
    data.allCutTimerUsed = False

    data.fruitAIQueue = []


def mousePressed(event, data):
    if data.mode == "homeScreen": homeScreenMousePressed(event, data)
    elif data.mode == "playClassic": playClassicMousePressed(event, data)
    elif data.mode == "playZen": playZenMousePressed(event, data)
    elif data.mode == "playTraining": playTrainingMousePressed(event, data)
    elif data.mode == "playAI": playAIMousePressed(event, data)
    elif data.mode == "aboutPage" :aboutPageMousePressed(event, data)

def keyPressed(event, data):
    if data.mode == "homeScreen": homeScreenKeyPressed(event, data)
    elif data.mode == "playClassic": playClassicKeyPressed(event, data)
    elif data.mode == "playZen": playZenKeyPressed(event, data)
    elif data.mode == "playTraining": playTrainingKeyPressed(event, data)
    elif data.mode == "playAI": playAIKeyPressed(event, data)
    elif data.mode == "aboutPage" :aboutPageKeyPressed(event, data)

def timerFired(data):
    data.player.updatePosition(data)
    data.player.updateTrail()
    data.timer += data.timerDelay
    if data.mode == "homeScreen": homeScreenTimerFired(data)
    elif data.mode == "playClassic": playClassicTimerFired(data)
    elif data.mode == "playZen": playZenTimerFired(data)
    elif data.mode == "playTraining": playTrainingTimerFired(data)
    elif data.mode == "playAI": playAITimerFired(data)
    elif data.mode == "aboutPage": aboutPageTimerFired(data)

def redrawAll(canvas, data):

    canvas.create_image(0, 0, image = data.backgroundImage, anchor = "nw", tags = "bckgrnd")
    if data.mode == "homeScreen": homeScreenRedrawAll(canvas, data)
    elif data.mode == "playClassic": playClassicRedrawAll(canvas, data)
    elif data.mode == "playZen": playZenRedrawAll(canvas, data)
    elif data.mode == "playTraining": playTrainingRedrawAll(canvas, data)
    elif data.mode == "playAI": playAIRedrawAll(canvas, data)
    elif data.mode == "aboutPage": aboutPageRedrawAll(canvas, data)




#____________________________PLAY GAME FUNCTION_________________________________
#-------------------------------------------------------------------------------



def initPlayClassic(data):

    data.classicBackButton = UIButton(1030, 20, 150, 100, "Back", "gray", "tempPath", data.button1)

def playClassicMousePressed(event, data):
    pass

def playClassicKeyPressed(event, data):

    if event.char == "r":
        init(data)


    elif event.char == "t":
        data.showTrace = not data.showTrace

    elif event.char == "p":
        data.paused = not data.paused


def playClassicTimerFired(data):

    if data.classicBackButton.loaded:
        data.mode = "homeScreen"

    data.classicBackButton.inButton(data.player.x, data.player.y)
    data.player.updatePosition(data)
    data.player.updateTrail()

    if not data.gameOver:
        if not data.paused:


            if data.timer % 1000 == 0:
                data.level = playLevel(data, data.level)

            for fru in data.fruit:
                fru.updatePosition()
                fru.inFruit(data.player.x, data.player.y)
                fru.checkCut()
                fru.cut(data)

            for piece in data.pieces:
                piece.updatePieces()

            

            clearCutFruit(data.fruit, data)
            clearMissedFruit(data.fruit, data)

            data.player.updatePosition(data)
            data.player.updateTrail()

            data.player.manageScoreCount(data)

            if data.player.lives <= 0:
                data.gameOver = True



def playClassicRedrawAll(canvas, data):
    
    data.classicBackButton.draw(canvas)
    canvas.create_image(0, 0, image = data.button1, anchor = "nw")

    traceStatus = "On" if data.showTrace else "Off"
    canvas.create_text(0, 140, text = "Press 't' to show Trace Mode! \n Press 'p' to pause \n Trace Mode: " + traceStatus, anchor = 'w', font = "Helvetica 16")

    
    if not data.gameOver:
        for fru in data.fruit:
            fru.draw(canvas)

        for piece in data.pieces:
            piece.draw(canvas)


        if data.showTrace:
            drawTrace(canvas, data)

        
        
        data.player.drawScore(canvas)
        data.player.drawLives(canvas)
    else:
        drawGameOverScreen(canvas, data)

    data.player.draw(canvas)
    data.player.drawTrail(canvas)
    data.player.drawCombos(canvas, data)


#____________________________PLAY ZEN___________________________________________
#-------------------------------------------------------------------------------



def initPlayZen(data):

    data.zenBackButton = UIButton(1030, 20, 150, 100, "Back", "gray", "tempPath", data.button1)
    

def playZenMousePressed(event, data):
    pass

def playZenKeyPressed(event, data):
    if event.char == "t":
        data.showTrace = not data.showTrace

    elif event.char == "p":
        data.paused = not data.paused

def playZenTimerFired(data):

    if data.zenBackButton.loaded:
        data.mode = "homeScreen"

    data.zenBackButton.inButton(data.player.x, data.player.y)
    data.player.updatePosition(data)
    data.player.updateTrail()


    if not data.gameOver:
        if not data.paused:

            data.zenTime += data.timerDelay
            timeLeft = data.zenTimeTotal - data.zenTime
            data.zenTimeString = convertMilli(timeLeft)


            if data.timer % 1500 == 0:
                level = random.randint(0,9)
                playLevel(data, level)

            for fru in data.fruit:
                fru.updatePosition()
                fru.inFruit(data.player.x, data.player.y)
                fru.checkCut()
                fru.cut(data)

            for piece in data.pieces:
                piece.updatePieces()

            clearCutFruit(data.fruit, data)
            clearMissedFruit(data.fruit, data)

            if data.timer > data.zenTimeTotal:
                data.gameOver = True

            data.player.manageScoreCount(data)



def playZenRedrawAll(canvas, data):

    data.zenBackButton.draw(canvas)
    canvas.create_image(0, 0, image = data.button1, anchor = "nw")
    traceStatus = "On" if data.showTrace else "Off"
    canvas.create_text(0, 140, text = "Press 't' to show Trace Mode! \n Press 'p' to pause \n Trace Mode: " + traceStatus, anchor = 'w', font = "Helvetica 16")

    if not data.gameOver:
        for fru in data.fruit:
            fru.draw(canvas)

        for piece in data.pieces:
            piece.draw(canvas)

        if data.showTrace:
            drawTrace(canvas, data)

        
        canvas.create_text(15, 50, anchor = "w", text = data.zenTimeString, font = "Helvetica 20")
        
    else:
        drawGameOverScreen(canvas, data)

    data.player.draw(canvas)
    data.player.drawTrail(canvas)
    data.player.drawScore(canvas)
    data.player.drawTrail(canvas)
    data.player.drawCombos(canvas, data)
#____________________________PLAY TRAINING______________________________________
#-------------------------------------------------------------------------------


def initPlayTraining(data):
    data.trainingBackButton = UIButton(1030, 20, 150, 100, "Back", "gray", "tempPath", data.button1)
    data.mostRecentBonusPoints = None
    data.roundScore = None

def playTrainingMousePressed(event, data):
    pass

def playTrainingKeyPressed(event, data):
    pass

def playTrainingTimerFired(data):

    if data.trainingBackButton.loaded:
        data.mode = "homeScreen"

    data.trainingBackButton.inButton(data.player.x, data.player.y)

    if not data.gameOver:
        if not data.paused:


            data.trainingTime += data.timerDelay
            data.skillTime += data.timerDelay
            if not data.allCutTimerUsed:
                data.allCutTimer += data.timerDelay


            if data.trainingTime % 3000 == 0:


                data.checkTime = data.trainingTime + 2000
                playLevel(data, int(data.skillRating))
                data.fruitsInAir = len(data.fruit)
                for fru in data.fruit:
                    if fru.isBomb:
                        data.bombCount += 1
                        data.fruitsInAir -= 1
            

            if data.trainingTime == data.checkTime:
                
                calculateSkillRating(data)


            for fru in data.fruit:
                fru.updatePosition()
                fru.inFruit(data.player.x, data.player.y)
                fru.checkCut()
                tempValue = fru.cut(data)
                if tempValue != None:
                    data.fruitsCut += tempValue


            for piece in data.pieces:
                piece.updatePieces()

            
            if data.fruitsInAir != 0 and data.fruitsCut == data.fruitsInAir and data.allCutTimer != 0 and not data.allCutTimerUsed:
                data.allCutTimer = data.skillTime
                data.allCutTimerUsed = True


            clearCutFruit(data.fruit, data)
            clearMissedFruit(data.fruit, data)


            data.player.updatePosition(data)
            data.player.updateTrail()
            data.player.manageScoreCount(data)


def playTrainingRedrawAll(canvas, data):

    data.trainingBackButton.draw(canvas)
    canvas.create_image(0, 0, image = data.button2, anchor = "nw")

    if not data.gameOver:
        for fru in data.fruit:
            fru.draw(canvas)

        for piece in data.pieces:
            piece.draw(canvas)

        canvas.create_text(14, 70, anchor = "w", text = "Skill Rating: " + str(data.skillRating), font = "Helvetica 20")
        
        canvas.create_text(14, 45, anchor = "w",
         text = convertMilli(data.trainingTime), font = "Helvetica 20")
        data.player.draw(canvas)
        data.player.drawTrail(canvas)
        data.player.drawScore(canvas)

    else:
        drawGameOverScreen(canvas, data)

    data.player.drawCombos(canvas, data)




#____________________________PLAY AI____________________________________________
#-------------------------------------------------------------------------------



def initAI(data):
    data.playerAI = PlayerAI(data)


def playAIMousePressed(event, data):
    pass

def playAIKeyPressed(event, data):

    if event.keysym == "Escape":
        data.mode = "homeScreen"

def playAITimerFired(data):

    if data.timer % 1000 == 0:
        data.level = playLevel(data, data.level)
        data.fruitAIQueue = copy.copy(data.fruit)

    for fru in data.fruit:
        fru.updatePosition()
        fru.inFruit(data.playerAI.x, data.playerAI.y)
        fru.checkCut()
        tempValue = fru.cut(data)

        if tempValue != None:
            data.playerAI.recentScoreCount += tempValue

    for piece in data.pieces:
        piece.updatePieces()

    i = 0
    while i < len(data.fruitAIQueue):

        if data.fruitAIQueue[i].isCut:

            data.fruitAIQueue.pop(i)

        else:

            i += 1


    clearCutFruit(data.fruit, data)

    clearMissedFruit(data.fruit, data)

    data.playerAI.updateTarget(data)
    data.playerAI.move(data)
    data.playerAI.updateTrail()
    data.playerAI.manageScoreCount(data)
    


def playAIRedrawAll(canvas, data):

    canvas.create_text(0, 120, text = "Press Escape to Exit AI Mode", anchor = 'w')
    for fru in data.fruit:
            fru.draw(canvas)

    for piece in data.pieces:
        piece.draw(canvas)


    if data.showTrace:
        drawTrace(canvas, data)

    data.playerAI.draw(canvas)
    data.playerAI.drawTrail(canvas)
    data.playerAI.drawScore(canvas)
    data.playerAI.displayAITracking(canvas, data)
    data.playerAI.displayLines(canvas, data)
    data.playerAI.drawCombos(canvas, data)
        



#____________________________HOMESCREEN________________________________________
#-------------------------------------------------------------------------------


def initHomeScreen(data):

    data.playButton = UIButton(data.width/2 - 150, 200, 300, 100, "Play", "gray", "tempPath", data.button2)
    data.aboutButton = UIButton(data.width/2 - 150, 450, 300, 100, "About", "gray", "tempPath", data.button2)

    data.classicSelect = StickyUIButton(data.width/2 - 300, 330, 150, 100, "Classic", "PaleTurquoise3", "PaleTurquoise4", data.button1, data.button3)
    data.zenSelect = StickyUIButton(data.width/2 - 150, 330, 150, 100, "Zen", "PaleTurquoise3", "PaleTurquoise4", data.button1, data.button3)
    data.trainingSelect = StickyUIButton(data.width/2, 330, 150, 100, "Training", "PaleTurquoise3", "PaleTurquoise4", data.button1, data.button3)
    data.AISelect = StickyUIButton(data.width/2 + 150, 330, 150, 100, "AI", "PaleTurquoise3", "PaleTurquoise4", data.button1, data.button3)

    data.classicSelect.pushed = True
    data.playMode = "classicSelect"


def homeScreenMousePressed(event, data):
    pass

def homeScreenKeyPressed(event, data):
    pass

def homeScreenTimerFired(data):

    if data.aboutButton.loaded:
        data.mode = "aboutPage"

    selectList = [data.classicSelect, data.zenSelect, data.trainingSelect, data.AISelect]
    modeList = ["playClassic", "playZen", "playTraining", "playAI"]

    currentSelectedIndex = None
    for i in range(len(selectList)):
        but = selectList[i]
        if but.pushed:
            currentSelectedIndex = i

    
    data.playButton.inButton(data.player.x, data.player.y)
    data.aboutButton.inButton(data.player.x, data.player.y)

    data.classicSelect.inButton(data.player.x, data.player.y)
    data.zenSelect.inButton(data.player.x, data.player.y)
    data.trainingSelect.inButton(data.player.x, data.player.y)
    data.AISelect.inButton(data.player.x, data.player.y)


    pushedIndexList = []
    for i in range(len(selectList)):
        but = selectList[i]
        if but.pushed:
            pushedIndexList.append(i)


    if currentSelectedIndex == None:
        data.playMode = "classicSelect"
    elif len(pushedIndexList) == 1:
        data.playMode = modeList[currentSelectedIndex]
    elif len(pushedIndexList) > 1:
        pushedIndexList.remove(currentSelectedIndex)
        data.playMode = modeList[pushedIndexList[0]]

    for i in range(len(selectList)):
        if data.playMode == modeList[i]:
            selectList[i].pushed = True
        else:
            selectList[i].pushed = False

    if data.playButton.loaded: #this is currently not working
        init(data)
        data.mode = modeList[currentSelectedIndex]



def homeScreenRedrawAll(canvas, data):


    canvas.create_image(data.width/2, 80, image = data.logo)
    canvas.create_text(data.width/2, 170, text = "by Emil Balian", font = "Arial 20")
    

    data.playButton.draw(canvas)
    data.aboutButton.draw(canvas)

    data.classicSelect.draw(canvas)
    data.zenSelect.draw(canvas)
    data.trainingSelect.draw(canvas)
    data.AISelect.draw(canvas)


    data.player.draw(canvas)
    data.player.drawTrail(canvas)

#____________________________ABOUT PAGE_________________________________________
#-------------------------------------------------------------------------------

def initAboutPage(data):
    data.aboutPageBackButton = UIButton(1030, 20, 150, 100, "Back", "gray", "tempPath", data.button1)

def aboutPageMousePressed(event, data):
    pass

def aboutPageKeyPressed(event, data):
    pass

def aboutPageTimerFired(data):
    if data.aboutPageBackButton.loaded:
        data.mode = "homeScreen"

    data.aboutPageBackButton.inButton(data.player.x, data.player.y)

    data.player.updatePosition(data)
    data.player.updateTrail()

def aboutPageRedrawAll(canvas, data):

    aboutPageMessage = """

    Hi! Welcome to my Term Project: Leap Motion Fruit Ninja!
    This page is for describing each mode and giving credits

    All the art for the game was done by my friend Jonas Petkus
    The run function was taken off the 15-112 website course notes
    The main external modules used are 'Leap' and 'Pillow' (PIL)

    Classic:

    This is your classic version of Fruit Ninja. Fruits come up and the waves of
    fruit get progressively harder as you play. If you hit a bomb or lose 3 lives, game over
    Note: In this mode you can press 't' to activate "Trace Mode" which draws a series
    of lines between the player cursor and the other fruit that represent the shortest
    and most optimal path to take from your current location to slice all the fruit.
    It is good if you are having trouble or just like playing with cool looking lines
    You may also press 'p' to pasue.

    Zen:

    This is the Zen Mode of Fruit Ninja, there are no lives, just try to cut as many fruit
    as possible, however slicing bombs reduces from your score.
    Trace mode also can be activated on this mode.

    Training:

    This mode calibrates your ability to play and complete levels into your "Skill rating"
    such that you find a skill rating you are at for playing the mode so you can practice
    on the levels that are at your skill cap. That being said, you must play a good amount
    of rounds before a player stabalizes at their Skill rating (0-10). There are a lot of factors 
    that go into the calculation of your skill rating after each round, such as if you 
    completed the level, if you hit a bomb, the time it takes to slice all the fruit, amount
    of fruit hit per round, etc. Since this mode aims to calibrate the players actual skill,
    trace mode is not an option on this mode.

    AI:

    This mode shows a built AI playing Fruit Ninja. All the main data that the AI takes into
    account when playing the game is shown on the top of the screen in the mode. The lines represent
    The distances to the fruit, the green dot represents the target, the green line represents the
    AI's path to the closest and most optimal fruit to it in order to play the game. All other info
    is seen at the top of the screen. Instead of loading the back button like other modes, you must
    press Escape to exit this mode.



    """
    canvas.create_text(data.width/2 + 50, 360, text = aboutPageMessage, anchor = "center", fill = "Blue")
    data.aboutPageBackButton.draw(canvas)
    data.player.draw(canvas)
    data.player.drawTrail(canvas)



#__________________________________THE RUN FUNCTION_____________________________
#__________this was taken from the 112 course website___________________________
#-------------------------------------------------------------------------------
####################################
# use the run function as-is
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete('all')
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    #parent = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)

    pilImage = Image.open("/Users/EMIL/Desktop/completelyNewTP2File/background.jpg")
    backgroundImage = ImageTk.PhotoImage(pilImage)

    canvas.pack()
    canvas.create_image(0, 0, image = backgroundImage, anchor = "nw", tags = "bckgrnd")
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 700)