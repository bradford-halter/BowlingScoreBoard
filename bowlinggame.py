from playercard import PlayerCard

# Object that takes in an integer representing the number of players and
# creates a List of PlayerCard Objects
#
# game            => List Object holding all the player cards
# totalNumPlayers => Integer value used for cycling between players
# currentFrame    => Integer value used for cycling between frames
# currentPlayer   => Integer value used for referring the the current player's
#                    card
# gameCompleted   => Boolean used for ending the current game

class BowlingGame:
    def __init__(self, numPlayers):
        self.game = []
        self.totalNumPlayers = numPlayers - 1
        self.currentFrame = 0
        self.currentPlayer = 0
        self.gameCompleted = False

        for self.x in range(numPlayers):
            print(f'Player {int(self.x + 1)} name (max 6 char): ')
            name = input()
            self.game.append(PlayerCard(name[:6]))
        
    # Attempts to pass in the number of knockedDown pins, if the number is
    # valid, the game uses some logic for tracking the current player and
    # frame, and lastly prints off the current game's scoreboard. Also returns
    # a boolean if which tracks if the input was valid
    def nextShot(self, knockedDown):
        validInput = self.game[self.currentPlayer].continueGame(knockedDown)
        
        if validInput:
            if self.game[self.currentPlayer].getCurrentFrame() == None:
                if self.totalNumPlayers == self.currentPlayer:
                    self.setGameComplete()
                
                self.currentPlayer += 1

                self.printScoreBoard()
            elif self.game[self.currentPlayer].getCurrentFrame() > self.currentFrame:
                if self.currentPlayer < self.totalNumPlayers:
                    self.currentPlayer += 1

                    self.printScoreBoard()
                else:
                    if self.game[self.totalNumPlayers].playerComplete():
                        self.gameCompleted = True
                    self.currentPlayer = 0
                    self.currentFrame += 1

                    self.printScoreBoard()
            else:
                self.printScoreBoard()

        return validInput

    # Prints the current scoreboard in a formatted manner
    def printScoreBoard(self):
        print('_________________________________________________________________________')
        print('| Player |  1  |  2  |  3  |  4  |  5  |  6  |  7  |' +
        '  8  |  9  |   10   |')
        print('|-----------------------------------------------------------------------|')
        for player in self.game:
            player.printScore()

    # Sets the current game to complete
    def setGameComplete(self):
        self.gameCompleted = True
    
    # Returns whether the current game is complete
    def gameComplete(self):
        return self.gameCompleted

    def getCurrentPlayer(self):
        return self.game[self.currentPlayer].getPlayerName()