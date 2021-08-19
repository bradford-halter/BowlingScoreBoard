from bowlingframe import BowlingFrame
from bowlingframetenth import BowlingFrameTenth

# Object that takes a player name and creates a score card for that player
#
# gameCard          => List Object that holds all the BowlingFrame Objects
#                      and the total score at that frame
# playerName        => String representing that player's name
# currentShot       => Tuple storing the current frame in index 0 and the
#                      current shot in index 1
# bonusShotUnlocked => Boolean that allows players to advance to the third
#                      shot in frame 10

class PlayerCard:
    def __init__(self, player):
        self.gameCard = []
        self.playerName = player
        
        self.currentShot = [0, 0] 
        
        for self.x in range(9):
            self.gameCard.append([BowlingFrame(), 0])

        self.gameCard.append([BowlingFrameTenth(), 0])
        self.bonusShotUnlocked = False

    # Takes in an integer for the number of pins that were knockedDown, then
    # determines where that integer should be stored
    def continueGame(self, knockedDown):
        validInput = False

        if self.currentShot[1] == 0:
            validInput = self.setFrameAFirstShot(knockedDown)
        elif self.currentShot[1] == 1:
            validInput = self.setFrameASecondShot(knockedDown)
        elif self.currentShot[1] == 2:
            validInput = self.setFrameAThirdShot(knockedDown)

        return validInput

    # Takes in the number of knockedDown pins and determines how this value
    # should be stored, depending on frame and knowing this is the first shot
    # in the current frame. Also returns if the input was valid as a boolean
    def setFrameAFirstShot(self, knockedDown):
        validInput = False
        frameNum = self.currentShot[0]
        
        if (frameNum >= 0) & (frameNum < 9):

            if (knockedDown >= 0) & (knockedDown <= 9):
                self.gameCard[frameNum][0].setFirstShot(knockedDown)
                self.updateTotalScore(frameNum)
                self.currentShot = [self.currentShot[0], 1]

                validInput = True
            elif knockedDown == 10:
                self.gameCard[frameNum][0].setFirstShot(knockedDown)
                self.updateTotalScore(frameNum)
                self.currentShot = [self.currentShot[0] + 1, 0]
                validInput = True
        elif frameNum == 9:
            if (knockedDown >= 0) & (knockedDown <= 10):
                self.gameCard[frameNum][0].setFirstShot(knockedDown)
                self.updateTotalScore(frameNum)
                self.currentShot = [self.currentShot[0], 1]
                validInput = True

        return validInput

    # Takes in the number of knockedDown pins and determines how this value
    # should be stored, depending on frame and knowing this is the second shot
    # in the current frame. Also returns if the input was valid as a boolean
    def setFrameASecondShot(self, knockedDown):
        validInput = False
        frameNum = self.currentShot[0]
        
        if (frameNum >= 0) & (frameNum < 9):
            if (knockedDown >= 0) & (knockedDown <= (10 - self.gameCard[frameNum][0].getFirstShot())):

                self.gameCard[frameNum][0].setSecondShot(knockedDown)
                self.updateTotalScore(frameNum)
                self.currentShot = [self.currentShot[0] + 1, 0]
                validInput = True
        elif frameNum == 9:
            firstShot = self.gameCard[9][0].getFirstShot()

            if firstShot != 10:
                if (knockedDown >= 0) & (knockedDown <= (10 - firstShot)):
                    self.gameCard[9][0].setSecondShot(knockedDown)

                    if (firstShot + knockedDown) == 10:
                        self.updateTotalScore(frameNum)
                        self.currentShot = [self.currentShot[0], 2]
                        self.bonusShotUnlocked = True
                    else:
                        self.updateTotalScore(frameNum)
                        self.currentShot = [None, None]

                    validInput = True
            else:
                if (knockedDown >= 0) & (knockedDown <= 10):
                    self.gameCard[9][0].setSecondShot(knockedDown)

                    self.updateTotalScore(frameNum)
                    self.currentShot = [self.currentShot[0], 2]
                    self.bonusShotUnlocked = True
                    validInput = True

        return validInput

    # Takes in the number of knockedDown pins and determines how this value
    # should be stored, depending on frame and knowing this is the third shot
    # in the current frame. Also returns if the input was valid as a boolean
    def setFrameAThirdShot(self, knockedDown):
        validInput = False
        frameNum = self.currentShot[0]

        if frameNum == 9:
            if self.bonusShotUnlocked == True:
                self.gameCard[9][0].setThirdShot(knockedDown)

                self.updateTotalScore(frameNum)
                self.currentShot = [None, None]
                validInput = True

        return validInput

    # Updates the current score card with standard bowling logic in regards to
    # strikes, spares, and the tenth frame
    def updateTotalScore(self, frameNum):
        for self.x in range(frameNum - 2, frameNum + 1):
            firstShot = self.gameCard[self.x][0].getFirstShot()
            
            if self.x - 1 >= 0:
                previousTotal = self.gameCard[self.x - 1][1]
            else:
                previousTotal = 0
            
            if (self.x >= 0) & (self.x <= 7):
                if firstShot < 10:
                    secondShot = self.gameCard[self.x][0].getSecondShot()
                    
                    if firstShot + secondShot < 10:
                        self.gameCard[self.x][1] = previousTotal + \
                            firstShot + secondShot
                    else:
                        self.gameCard[self.x][1] = previousTotal + 10 + \
                            self.gameCard[self.x + 1][0].getFirstShot()
                else:
                    secondShot = self.gameCard[self.x + 1][0].getFirstShot()
                    
                    if secondShot < 10:
                        self.gameCard[self.x][1] = previousTotal + firstShot \
                            + secondShot + \
                            self.gameCard[self.x + 1][0].getSecondShot()
                    else:
                        self.gameCard[self.x][1] = previousTotal + 20 + \
                            self.gameCard[self.x + 2][0].getFirstShot()
            elif self.x == 8:
                if firstShot < 10:
                    secondShot = self.gameCard[self.x][0].getSecondShot()

                    if firstShot + secondShot < 10:
                        self.gameCard[self.x][1] = previousTotal + \
                            firstShot + secondShot
                    else:
                        self.gameCard[self.x][1] = previousTotal + 10 + \
                            self.gameCard[self.x + 1][0].getFirstShot()
                else:
                    self.gameCard[self.x][1] = previousTotal + 10 + \
                        self.gameCard[self.x + 1][0].getFirstShot() + \
                        self.gameCard[self.x + 1][0].getSecondShot()
            elif self.x == 9:
                secondShot = self.gameCard[self.x][0].getSecondShot()
                thirdShot = self.gameCard[self.x][0].getThirdShot()
                
                if firstShot < 10:
                    self.gameCard[self.x][1] = previousTotal + \
                        firstShot + secondShot + thirdShot
                else:
                    self.gameCard[self.x][1] = previousTotal + 10 + \
                        secondShot + thirdShot

    def getPlayerName(self):
        return self.playerName
    
    # Prints a formatted version of the players score card
    def printScore(self):
        gC = self.gameCard
        gCgetFirst = lambda frameNum: gC[frameNum][0].getFirstShot()
        gCgetSecond = lambda frameNum: gC[frameNum][0].getSecondShot()
        gCgetThird = lambda frameNum: gC[frameNum][0].getThirdShot()
        gCgetTotal = lambda frameNum: gC[frameNum][1]
        
        print('|        |{0:2d}|{1:2d}|{2:2d}|{3:2d}|{4:2d}|{5:2d}|{6:2d}|{7:2d}|{8:2d}|{9:2d}|{10:2d}|{11:2d}|{12:2d}|{13:2d}|{14:2d}|{15:2d}|{16:2d}|{17:2d}|{18:2d}|{19:2d}|{20:2d}|'.format(
            gCgetFirst(0), gCgetSecond(0),
            gCgetFirst(1), gCgetSecond(1),
            gCgetFirst(2), gCgetSecond(2),
            gCgetFirst(3), gCgetSecond(3),
            gCgetFirst(4), gCgetSecond(4),
            gCgetFirst(5), gCgetSecond(5),
            gCgetFirst(6), gCgetSecond(6),
            gCgetFirst(7), gCgetSecond(7),
            gCgetFirst(8), gCgetSecond(8),
            gCgetFirst(9), gCgetSecond(9), gCgetThird(9))
        )
        print('| {0:6s} | {1:3d} | {2:3d} | {3:3d} | {4:3d} | {5:3d} | {6:3d} | {7:3d} | {8:3d} | {9:3d} |    {10:3d} |'.format(
            self.playerName, gCgetTotal(0), gCgetTotal(1), gCgetTotal(2), 
            gCgetTotal(3), gCgetTotal(4), gCgetTotal(5), gCgetTotal(6), 
            gCgetTotal(7), gCgetTotal(8), gCgetTotal(9))
        )
        print('|-----------------------------------------------------------------------|')
    
    def getCurrentFrame(self):
        return self.currentShot[0]

    # This returns if the player has completed their game as a boolean
    def playerComplete(self):
        complete = False

        if self.currentShot[1] == None:
            complete = True
        
        return complete