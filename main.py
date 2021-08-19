from bowlinggame import BowlingGame

# Runs the bowling scoreboard allowing users to track their scores manually
# with a couple of restrictions to keep the board readable

def main():
    print('Welcome to my bowling score board')

    while True:

        print('Would you like to start a game? (y/n)')
        
        expression = input()

        if expression.__eq__('n'):
            break
        else:
            print('How many players? (max of 9)')

            numPlayers = input()

            try:
                numPlayers = int(numPlayers)
            except:
                print('Invalid input')

            if type(numPlayers) == int:
                if numPlayers <= 0:
                    print('Cannot have less than 1 player.')
                elif numPlayers > 9:
                    print('Cannot have more than 9 players.')
                else:
                    bowlingGame = BowlingGame(numPlayers)
                    gameCompleted = bowlingGame.gameComplete()

                    while gameCompleted != True:
                        print(f'{bowlingGame.getCurrentPlayer()} is up right now!')
                        print('Input how many pins were knocked down:')
                        knockedDown = input()
                        
                        try:
                            knockedDown = int(knockedDown)
                        except:
                            print('Invalid Input')

                        if type(knockedDown) == int:
                            validInput = bowlingGame.nextShot(knockedDown)
                            
                            if validInput != True:
                                print('Invalid Input')
                        
                        gameCompleted = bowlingGame.gameComplete()

                        if gameCompleted != True:
                            while True:
                                print('Next Shot? (y/n)')
                                expression = input()

                                if expression.__eq__('y'):
                                    break
                                elif expression.__eq__('n'):
                                    bowlingGame.setGameComplete()
                                    break

                        gameCompleted = bowlingGame.gameComplete()

    print('Have a nice day!')

if __name__ == "__main__":
    main()