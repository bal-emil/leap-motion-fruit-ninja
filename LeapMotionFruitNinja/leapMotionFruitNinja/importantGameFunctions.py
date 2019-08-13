from UIButtonsClasses import *
from Tkinter import *
from mainClasses import *
from PIL import Image, ImageTk
import copy

#this file contains all the important game functions for the game to run
#such as clearing fruit, throwing fruit, and generally handling objects
#that were created in an appropriate way. Things such as the skill rating,
#trace, and other functions that are important but dont fit into any other file
#are also found here

#____________________________Important Game Functions___________________________
#-------------------------------------------------------------------------------



def throwFruit(fruit, vel, acc):

    fruit.velocity = vel
    fruit.acceleration = acc


def spawnFruit(data, x, y):

    fruitPick = random.choice(data.fruitSelect)

    chosenFruit = Fruit(x, y, 50, fruitPick)

    data.fruit.append(chosenFruit)


def spawnBomb(data, x, y):

    bomb = Fruit(x, y, 50, data.bombImage)
    bomb.isBomb = True
    data.fruit.append(bomb)



def playBasicLevel(data):

    numFruits = 2
    for i in range(numFruits):
        spawnFruit(data, 200, 800)
        spawnFruit(data, 1000, 800)

    for fru in data.fruit:
        if not fru.thrown:
            if fru.cx < 300:

                throwFruit(fru, (random.randint(0, 3), -17 + random.randint(-2, 2)), (0, data.gravity))
            else:

                throwFruit(fru, (random.randint(-3, 0), -17 + random.randint(-2, 2)), (0, data.gravity))



def playLevelEasy1(data):

    numFruits = 1
    for i in range(numFruits):
        spawnFruit(data, 350, 800)


    for fru in data.fruit:
        if not fru.thrown:
            throwFruit(fru, (0, -15), (0, data.gravity))



def playLevelEasy2(data):

    numFruits = 1
    for i in range(numFruits):
        spawnFruit(data, 400, 800)

    for fru in data.fruit:
        if not fru.thrown:
            throwFruit(fru, (0, -15), (0, data.gravity))


def playLevelMedium1(data):

    numFruits = 1
    for i in range(numFruits):
        spawnFruit(data, 350, 800)
        spawnFruit(data, 200, 800)

    for fru in data.fruit:
        if not fru.thrown:
            throwFruit(fru, (0, -15), (0, data.gravity))



def playLevelMedium2(data):

    numFruits = 1
    for i in range(numFruits):
        spawnFruit(data, 150, 800)
        spawnFruit(data, 400, 800)

    if data.mode != "playAI" and random.randrange(0, 100) < 30:
        spawnBomb(data, random.randint(200, 1000), 800)

    for fru in data.fruit:
        if not fru.thrown:
            throwFruit(fru, (0, -15), (0, data.gravity))



def playLevelMedium3(data):

    numFruits = 1
    for i in range(numFruits):
        spawnFruit(data, 150, 800)
        spawnFruit(data, 400, 800)


    if data.mode != "playAI" and random.randrange(0, 100) < 30:
        spawnBomb(data, random.randint(200, 1000), 800)

    for fru in data.fruit:
        if not fru.thrown:
            throwFruit(fru, (random.randint(0, 3), -15), (0, data.gravity))


def playLevelHard1(data):

    numFruits = 2
    for i in range(numFruits):
        spawnFruit(data, 200, 800)
        spawnFruit(data, 1000, 800)


    if data.mode != "playAI" and random.randrange(0, 100) < 35:
        spawnBomb(data, random.randint(200, 1000), 800)


    for fru in data.fruit:
        if not fru.thrown:
            if fru.cx < 300:
                throwFruit(fru, (random.randint(0, 3), -17 + random.randint(-2, 2)), (0, data.gravity))
            else:
                throwFruit(fru, (random.randint(-3, 0), -17 + random.randint(-2, 2)), (0, data.gravity))


def playLevelHard2(data):

    numFruits = 2
    for i in range(numFruits):
        spawnFruit(data, 200, 800)
        spawnFruit(data, 1000, 800)


    if data.mode != "playAI" and random.randrange(0, 100) < 35:
        spawnBomb(data, random.randint(200, 1000), 800)

    for fru in data.fruit:
        if not fru.thrown:
            if fru.cx < 300:
                throwFruit(fru, (random.randint(-2, 4), -17 + random.randint(-2, 2)), (0, data.gravity))
            else:
                throwFruit(fru, (random.randint(-3, 2), -17 + random.randint(-2, 2)), (0, data.gravity))


def playLevelHard3(data):

    numFruits = 2
    for i in range(numFruits):
        spawnFruit(data, 200, 800)
        spawnFruit(data, 1000, 800)


    if data.mode != "playAI" and random.randrange(0, 100) < 50:
        spawnBomb(data, random.randint(200, 1000), 800)

    for fru in data.fruit:
        if not fru.thrown:
            if fru.cx < 300:
                throwFruit(fru, (random.randint(-2, 4), -17 + random.randint(-2, 2)), (0, data.gravity))
            else:
                throwFruit(fru, (random.randint(-3, 2), -17 + random.randint(-2, 2)), (0, data.gravity))


def playLevelInsane1(data):

    numFruits = 2
    for i in range(numFruits):
        spawnFruit(data, 200, 800)
        spawnFruit(data, 450, 800)
        spawnFruit(data, 1000, 800)


    if data.mode != "playAI" and random.randrange(0, 100) < 50:
        spawnBomb(data, random.randint(200, 1000), 800)
        spawnBomb(data, random.randint(200, 1000), 800)

    for fru in data.fruit:
        if not fru.thrown:
            if fru.cx < 300:
                throwFruit(fru, (random.randint(-2, 4), -15 + random.randint(-2, 2)), (0, data.gravity))
            else:
                throwFruit(fru, (random.randint(-3, 2), -15 + random.randint(-2, 2)), (0, data.gravity))



def playLevelInsane2(data):

    numFruits = 2
    for i in range(numFruits):
        spawnFruit(data, 200, 800)
        spawnFruit(data, 450, 800)
        spawnFruit(data, 1000, 800)


    if data.mode != "playAI" and random.randrange(0, 100) < 70:
        spawnBomb(data, random.randint(200, 1000), 800)
        spawnBomb(data, random.randint(200, 1000), 800)

    for fru in data.fruit:
        if not fru.thrown:
            if fru.cx < 300:
                throwFruit(fru, (random.randint(-3, 4), -17 + random.randint(-3, 3)), (0, data.gravity))
            else:
                throwFruit(fru, (random.randint(-3, 2), -17 + random.randint(-4, 4)), (0, data.gravity))



def playLevel(data, level):
    if level == 0:
        playLevelEasy1(data)
    elif level == 1:
        playLevelEasy2(data)
    elif level == 2:
        playLevelMedium1(data)
    elif level == 3:
        playLevelMedium2(data)
    elif level == 4:
        playLevelMedium3(data)
    elif level == 5:
        playLevelHard1(data)
    elif level == 6:
        playLevelHard2(data)
    elif level == 7:
        playLevelHard3(data)
    elif level == 8:
        playLevelInsane1(data)
    elif level == 9:
        playLevelInsane2(data)
    else:
        playLevelInsane2(data)

    nextLevel = level + 1
    return nextLevel



def clearCutFruit(fruitList, data):

    i = 0
    while i < len(fruitList):

        if fruitList[i].isCut and not fruitList[i].isBomb:

            fruitList.pop(i)
            data.player.recentScoreCount += 1

        elif fruitList[i].isCut and fruitList[i].isBomb and \
        (data.mode == "playZen" or data.mode == "playTraining"):

            fruitList.pop(i)
            data.player.totalScore -= 10
            if data.player.totalScore < 0:
                data.player.totalScore = 0

        else:

            i += 1


def clearMissedFruit(fruitList, data):

    i = 0
    while i < len(fruitList):

        if fruitList[i].cy > data.height and fruitList[i].velocity[1] > 0:

            if fruitList[i].isBomb:
                fruitList.pop(i)
            else:
                fruitList.pop(i)
                data.player.lives -= 1

        else:

            i += 1


def drawGameOverScreen(canvas, data):

    if data.gameOver:

        canvas.create_text(data.width/2, data.height/2,
         text = "Game Over \n Score: " + str(data.player.recentScoreCount), 
            font = "Helvetica 40")


def generateTrace(data):

    points = []

    for fru in data.fruit:
        if not fru.isBomb:
            points.append((fru.cx, fru.cy))


    trace = []
    lastPoint = (data.player.x, data.player.y)

    if len(points) == 0:
        return
    elif len(points) == 1:
        return [lastPoint] + points
    elif len(points) == 2:

        distance1 = distance(lastPoint[0], lastPoint[1], points[0][0], points[0][1])
        distance2 = distance(lastPoint[0], lastPoint[1], points[1][0], points[1][1])

        if distance1 < distance2:
            return [lastPoint] + points
        else:
            return [lastPoint] + [points[1]] + [points[0]]

    else:

        while len(points) != 1:
            distanceList = []
            advDistanceList = []
            for i in range(len(points)):
                distanceList.append(distance(lastPoint[0], lastPoint[1], points[i][0], points[i][1]))
                advDistanceList.append((i, distance(lastPoint[0], lastPoint[1], points[i][0], points[i][1])))

            minDistance = min(distanceList)

            minIndex = 0
            for i in range(len(advDistanceList)):
                if advDistanceList[i][1] == minDistance:
                    minIndex = i

            trace.append(lastPoint)
            trace.append(points[minIndex])

            lastPoint = points[minIndex]
            points.pop(minIndex)

    trace.append(points[0])
    return trace




def drawTrace(canvas, data):

    points = generateTrace(data)

    if points == None:
        return
    elif len(points) == 1:
        return


    for i in range(1, len(points)):
        p1x = points[i-1][0]
        p1y = points[i-1][1]
        p2x = points[i][0]
        p2y = points[i][1]

        canvas.create_line(p1x, p1y, p2x, p2y, fill = "red", width = 4)


def calculateSkillRating(data):
    
    if data.skillTime > 2000:
        

        if data.fruitsInAir - data.fruitsCut >= 1:

            data.skillRating -= 0.52
            data.skillRating -= 0.21 * abs(data.fruitsInAir - data.fruitsCut)


        else:

            data.skillRating += 0.4

            
            bonusSpeedPoints = abs(data.skillRating*(2000.0 - float(data.allCutTimer))/3000.0)

            if data.trainingTime < 6000:
                bonusSpeedPoints = 0


            data.mostRecentBonusPoints = bonusSpeedPoints
            data.skillRating += bonusSpeedPoints
            data.roundScore = 0.4 + bonusSpeedPoints

        if data.skillRating < 0:
            data.skillRating = 0
        elif data.skillRating > 10:
            data.skillRating = 10


        data.skillTime = 0
        data.fruitsCut = 0
        data.fruitsInAir = 0
        data.bombCount = 0
        data.allCutTimer = 0
        data.allCutTimerUsed = False

