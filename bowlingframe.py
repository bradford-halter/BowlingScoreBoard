# BowlingFrame Object that stores a frame List which holds a value for the
# first and second shots
#
# frame => stores the first shot in index 0 and the second shot in index 
# 1 with integer values that default to 0

class BowlingFrame:
    def __init__(self):
        self.frame = [0, 0]

    def setFirstShot(self, knockedDown):
        self.frame[0] = knockedDown
    
    def setSecondShot(self, knockedDown):
        self.frame[1] = knockedDown

    def getFirstShot(self):
        return self.frame[0]

    def getSecondShot(self):
        return self.frame[1]