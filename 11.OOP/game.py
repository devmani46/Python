class Keyboard():
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveDown(self):
        pass

Keyboard1=Keyboard()
Player1=Player()

if(Keyboard1.isLeftPressed()):
    Player1.moveLeft()

if(Keyboard1.isRightPressed()):
    Player1.moveRight()

if(Keyboard1.isTopPressed()):
    Player1.moveTop()

if(Keyboard1.isDownPressed()):
    Player1.moveDown()

