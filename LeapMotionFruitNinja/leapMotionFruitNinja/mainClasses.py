
import Leap, sys, thread, time, math, random, os
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#this file holds all the nessesary small functions needed for the main classes,
#such as the fruit, player, AI, pieces, just all the main big classes for the
#game



#Miscellaneous helper functions
#-------------------------------------------------------------------------------

def distance(x1, y1, x2, y2):

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def calculateSlope(x1, y1, x2, y2):

    rise = abs(y2-y1)
    run = abs(x2-x1)

    if run == 0:
        return 0
    slope = rise/run
    return slope



def getFingerPosition(controller):

    frame = controller.frame()

    for hand in frame.hands:
            
        handType = "Left Hand" if hand.is_left else "Right Hand"

        for finger in hand.fingers:

            if finger.type == 1:
                return finger.stabilized_tip_position


def translateCoords(x, y, data):

    leapX = x
    leapY = y
    leapYRange = data.leapYEnd - data.leapYStart
    leapXRange = data.leapXEnd - data.leapXStart
    appX = leapX * (data.width/leapXRange) + data.width//2
    appY = data.height - (leapY * (data.height/leapYRange))

    return (appX, appY)


def convertMilli(milli):

    sec=(milli/1000)%60
    minutes=(milli/(1000*60))%60
    returnString = ("%d:%d" % (minutes, sec))
    if returnString[1] == ":":
        returnString = "0" + returnString
    if returnString[2] == ":" and len(returnString[2:]) == 2:
        returnString = returnString[:3] + "0" + returnString[3:]

    return returnString

def getFruitType(data, fru):

    fruitType = ""
    if fru.fruitImage == data.water:
        fruitType = "Watermelon"
    elif fru.fruitImage == data.coco:
        fruitType = "Coconut"
    elif fru.fruitImage == data.orange:
        fruitType = "Orange"
    elif fru.fruitImage == data.bombImage:
        fruitType = "Bomb"

    return fruitType





#____________________________MAIN CLASSES FOR THE GAME__________________________


#---------------------------THE PLAYER CLASS------------------------------------
#Keeps track of all the info about the player, as in position, lives, trail, etc
class Player(object):

    def __init__(self, data):
        self.x = data.width/2 #where it is on the app's coordinates
        self.y = data.height/2
        self.r = 5 #default radius for the cursor
        self.color = "Black"
        self.lives = 3
        self.totalScore = 0
        self.recentScoreCount = 0 #keep track to do time-based combo additions
        self.trail = []

        self.lastPosition = None

        self.lastScore = 0
        self.comboTime = 500
        self.comboCount = 0
        self.comboList = []
        self.firstComboCut = False

    #this function looks to the leap motion and pulls the position and
    #translates it into the app's coordinate system.
    #additionallly, it adds that point into the 'trail'
    def updatePosition(self, data):

        newPos = getFingerPosition(data.controller)

        if not isinstance(newPos, Leap.Vector):
            if self.lastPosition != None:
                self.x = self.lastPosition[0]
                self.y = self.lastPosition[1]
            else:
                self.x = data.width/2
                self.y = data.height/2
        else:

            leapX = newPos[0]
            leapY = newPos[1]
            newCoords = translateCoords(leapX, leapY, data)

            self.x = newCoords[0]
            self.y = newCoords[1]

        self.lastPosition = (self.x, self.y)
        self.trail.append((self.x, self.y, self.r)) #appends to the trail

    def draw(self, canvas):

        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
            self.y + self.r, fill = self.color)

    #updateTrail removes all the trails from the trail list that are invisable
    #and decreases each of the radii of the circles in the trail by 1 to give
    #a trail effect
    def updateTrail(self):

        i = 0
        while i < len(self.trail):
            if self.trail[i][2] <= 0:
                self.trail.pop(i)
            else:
                x = self.trail[i][0]
                y = self.trail[i][1]
                r = self.trail[i][2]
                self.trail[i] = (x, y, r-1) #makes the radius smaller for the
                i += 1                  #older trails so it looks like a trail


    #this simply goes through the trail list and draws all the circles in it
    def drawTrail(self, canvas):
        for cir in self.trail:
            x = cir[0]
            y = cir[1]
            r = cir[2]
            canvas.create_oval(x - r, y - r, x + r, y + r, fill = self.color)


    def drawScore(self, canvas):
        canvas.create_text(14, 10, anchor = "nw", 
            text = "Score: " + str(self.totalScore), font = "Helvetica 20")

    def drawLives(self, canvas):
        canvas.create_text(14, 44, anchor = "nw",
         text = "Lives: " + str(self.lives), font = "Helvetica 20")


    def manageScoreCount(self, data):

        if self.comboTime > 0:
            
            if self.lastScore < self.recentScoreCount:
                self.lastScore = self.recentScoreCount
                self.comboTime = 500
                if not self.firstComboCut:
                    self.totalScore += 1
                    self.firstComboCut = True
                else:
                    self.totalScore += 2
                self.comboCount += 1
                self.comboList.append((self.comboCount, data.player.x, data.player.y, 150))

        else:
            self.firstComboCut = False
            self.lastScore = self.recentScoreCount
            self.comboCount = 0
            self.comboTime = 500

        self.comboTime -= data.timerDelay

        i = 0
        while i < len(self.comboList):
            if self.comboList[i][3] <= 0:
                self.comboList.pop(i)
            else:
                self.comboList[i] = (self.comboList[i][0], self.comboList[i][1],
                 self.comboList[i][2], self.comboList[i][3] - data.timerDelay)

                i += 1

    def drawCombos(self, canvas, data):

        for elem in self.comboList:
            x = elem[1]
            y = elem[2]
            count = elem[0]

            if count == 2:
                canvas.create_text(x + 60, y - 60, text = "Combo! " + str(count), font = "Arial 30", fill = "maroon3")
            elif count != 1:
                canvas.create_text(x + 60, y - 60, text = str(count), font = "Arial 30", fill = "maroon3")





#-------------------------------------------------------------------------------

class PlayerAI(Player):
    def __init__(self, data):
        self.x = data.width/2 #where it is on the app's coordinates
        self.y = data.height/2
        self.r = 5 #default radius for the cursor
        self.color = "Black"
        self.lives = 3
        self.totalScore = 0
        self.recentScoreCount = 0 #keep track to do time-based combo additions
        self.trail = []

        self.lastPosition = None

        self.speed = 30

        self.target = None
        self.targetPos = (data.width//2, data.height//2)
        self.targetID = None
        self.validTargets = []
        self.minIndex = None
        self.distanceList = []

        self.lastScore = 0
        self.comboTime = 500
        self.comboCount = 0
        self.comboList = []
        self.firstComboCut = False

    def updateTarget(self, data):

        self.distanceList = []
        self.validTargets = []

        if self.target != None:
            if distance(self.x, self.y, self.targetPos[0], self.targetPos[1]) < self.target.r - 10:
                data.fruitAIQueue.pop(data.fruitAIQueue.index(self.target))
                


        if len(data.fruitAIQueue) == 0:
            self.target = None
            self.targetPos = (data.width//2, data.height//2)
            self.targetID = None
            return
        else:
            for fru in data.fruitAIQueue:
                if not fru.isBomb:
                    self.validTargets.append((fru, fru.fruitID))
                    self.distanceList.append(distance(fru.cx, fru.cy, data.playerAI.x, data.playerAI.y))

        if len(self.distanceList) > 0:
            self.minIndex = self.distanceList.index(min(self.distanceList))
            self.target = self.validTargets[self.minIndex][0]
            self.targetID = self.validTargets[self.minIndex][0].fruitID
            self.targetPos = (self.validTargets[self.minIndex][0].cx, self.validTargets[self.minIndex][0].cy)
        else:
            self.target = None
            self.targetPos = (data.width//2, data.height//2)
            self.targetID = None


        

        
    def move(self, data):
        if self.targetPos[0] - self.x > 0:
            self.x += self.speed
        else:
            self.x -= self.speed

        if self.targetPos[1] - self.y > 0:
            self.y += self.speed
        else:
            self.y -= self.speed


    def displayAITracking(self, canvas, data):

        objectList = []
        for fru in data.fruit:

            fruitType = getFruitType(data, fru)

            objectList.append((fruitType, fru.fruitID))

        canvas.create_text(200, 20, text = "AI viewed objects: " + str(objectList),
         anchor = "w", fill = "red", font = "Arial 20")

        targetFruitType = None
        if self.target != None:
            targetFruitType = getFruitType(data, self.target)
        canvas.create_text(200, 40, text = "Current Target: " + str((targetFruitType, self.targetID)),
            anchor = "w", fill = "red", font = "Arial 20")
        canvas.create_text(200, 60, text = "Distances to fruit: " + str(self.distanceList),
         anchor = "w", fill = "red", font = "Arial 20")
        if self.target == None:
            distanceToTarget = None
        else:
            distanceToTarget = distance(self.x, self.y, self.targetPos[0], self.targetPos[1])
        canvas.create_text(200, 80, text = "Distance to target: " + str(distanceToTarget),
            anchor = "w", fill = "red", font = "Arial 20")

    def displayLines(self, canvas, data):

        for fru in data.fruit:
            if not fru.isBomb:
                canvas.create_line(data.playerAI.x, data.playerAI.y, fru.cx, fru.cy, fill = "red")

        canvas.create_line(data.playerAI.x, data.playerAI.y, self.targetPos[0], self.targetPos[1], fill = "green")

        if self.targetPos[0] != data.width//2 and self.targetPos[1] != data.width//2:
            canvas.create_oval(self.targetPos[0] - 10, self.targetPos[1] - 10, self.targetPos[0] + 10, self.targetPos[1] + 10, fill = "green")


    def manageScoreCount(self, data):

        if self.comboTime > 0:
            
            if self.lastScore < self.recentScoreCount:
                self.lastScore = self.recentScoreCount
                self.comboTime = 500
                if not self.firstComboCut:
                    self.totalScore += 1
                    self.firstComboCut = True
                else:
                    self.totalScore += 2
                self.comboCount += 1
                self.comboList.append((self.comboCount, data.playerAI.x, data.playerAI.y, 150))

        else:
            self.firstComboCut = False
            self.lastScore = self.recentScoreCount
            self.comboCount = 0
            self.comboTime = 500

        self.comboTime -= data.timerDelay

        i = 0
        while i < len(self.comboList):
            if self.comboList[i][3] <= 0:
                self.comboList.pop(i)
            else:
                self.comboList[i] = (self.comboList[i][0], self.comboList[i][1],
                 self.comboList[i][2], self.comboList[i][3] - data.timerDelay)

                i += 1


#--------------------THE FRUIT CLASS--------------------------------------------

#for our intents and purposes, a standard fruit object is a perfectly circular
#piece of fruit
class Fruit(object):

    def __init__(self, cx, cy, r, fruitImage):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fruitImage = fruitImage

        self.isCut = False
        self.piecesCreated = False
        self.thrown = False
        self.isBomb = False
        self.velocity = None #tuple of vel/accel values in form (x, y)
        self.acceleration = None

        self.entryPoint = None
        self.exitPoint = None
        self.playerInside = False
        self.lastPointInside = None

        self.fruitID = str(random.randint(1000,9999)) + str(random.randint(0,9))


    #Given an x and y coord of the player, the inFruit function handles
    #everything to do with determining the entry/exit points of the slice of the
    #player
    def inFruit(self, x, y):

        if distance(self.cx, self.cy, x, y) < self.r:
            if not self.playerInside:
                self.entryPoint = (x, y)

            self.lastPointInside = (x, y)
            self.playerInside = True

            return True

        if self.lastPointInside != None and self.exitPoint == None:
            self.exitPoint = self.lastPointInside
            self.color = "Red"

        return False


    def checkCut(self):

        if self.exitPoint != None and self.entryPoint != None:
            self.isCut = True
            return True
        self.isCut = False
        return False



    def draw(self, canvas):

        x = self.cx
        y = self.cy
        r = self.r
        canvas.create_image(x, y, image = self.fruitImage)


    def updatePosition(self):

        if self.velocity == None:
            return

        if self.acceleration == None or self.acceleration == (0,0) and \
         self.velocity != None:

            self.cx += self.velocity[0]
            self.cy += self.velocity[1]
            return

        self.cx += self.velocity[0]
        self.cy += self.velocity[1]
        newVelX = self.velocity[0] + self.acceleration[0]
        newVelY = self.velocity[1] + self.acceleration[1]
        self.velocity = (newVelX, newVelY)

        if self.cy < 700:
            self.thrown = True


    def cut(self, data):

        if self.isBomb and self.isCut and data.mode != "playZen" and data.mode != "playTraining":
            data.gameOver = True

        elif self.isBomb and self.isCut and (data.mode == "playZen" or data.mode == "playTraining"):
            return -5

        if self.isCut and not self.piecesCreated and not self.isBomb:

            self.piecesCreated = True

            pieceList = data.pieceSelect[self.fruitImage]

            slope = calculateSlope(self.entryPoint[0], self.entryPoint[1], self.exitPoint[0], self.exitPoint[1])

            data.pieces.append(Pieces(self.cx, self.cy, self.r, self.velocity,
             self.acceleration, slope, pieceList))

            return 1


            



#-------------------------------------------------------------------------------
#--------------------THE PIECES CLASS-------------------------------------------


class Pieces(object):

    def __init__(self, cx, cy, r, vel, acc, slope, pieceList):
        self.cx1 = cx
        self.cx2 = cx
        self.cy1 = cy
        self.cy2 = cy
        self.slope = slope

        if self.slope < 1:
            self.bit1 = pieceList[0]
            self.bit2 = pieceList[1]
        else:
            self.bit1 = pieceList[2]
            self.bit2 = pieceList[3]

        self.r = r

        if self.slope < 1:

            self.velocity1 = (vel[0] + 1, vel[1] - 0.4)
            self.velocity2 = (vel[0] + 1, vel[1])

        else:
            self.velocity1 = (vel[0] - 0.2, vel[1])
            self.velocity2 = (vel[0], vel[1])

        self.acceleration1 = acc
        self.acceleration2 = (acc[0], acc[1])
        

    def draw(self, canvas):

        cx1 = self.cx1
        cy1 = self.cy1
        cx2 = self.cx2
        cy2 = self.cy2
        r = self.r

        if self.slope < 1:
            canvas.create_image(cx1-r,cy1-r, anchor = "nw", image = self.bit2)
            canvas.create_image(cx2-r,cy2, anchor = "nw", image = self.bit1)
        else:
            canvas.create_image(cx1-r, cy1-r, anchor = "nw", image = self.bit1)
            canvas.create_image(cx2, cy2-r, anchor = "nw", image = self.bit2 )

    def updatePieces(self):

        self.cx1 += self.velocity1[0]
        self.cy1 += self.velocity1[1]
        self.cx2 += self.velocity2[0]
        self.cy2 += self.velocity2[1]


        newVelX1 = self.velocity1[0] + self.acceleration1[0]
        newVelY1 = self.velocity1[1] + self.acceleration1[1]

        newVelX2 = self.velocity2[0] + self.acceleration2[0]
        newVelY2 = self.velocity2[1] + self.acceleration2[1]


        self.velocity1 = (newVelX1, newVelY1)
        self.velocity2 = (newVelX2, newVelY2)


