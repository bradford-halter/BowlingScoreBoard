from bowlingframe import BowlingFrame

# BowlingFrame Object that stores a third shot value in addition to
# all the features of a standard bowling frame
#
# frame => stores the first shot in index 0, the second shot in index 
# 1, and the third in index 2 with integer values that default to 0

class BowlingFrameTenth(BowlingFrame):
    def __init__(self):
        self.frame = [0, 0, 0]

    def setThirdShot(self, knockedDown):
        self.frame[2] = knockedDown

    def getThirdShot(self):
        return self.frame[2]