'''
Autor: Victor Santiago;
v1.0

'''

class Perception:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.down = -1

    def capturePerception(self, world, currentRow, currentColumn):
        if currentColumn == 0:
            self.left = -1
            self.right = currentColumn + 1
            if currentRow == (world.length-1):
                self.down = -1
            else:
                self.down = currentRow + 1
        elif currentRow == (world.length-1):
            self.left = currentColumn - 1
            if currentColumn == (world.length-1):
                self.right =  -1
            else:
                self.right = currentColumn + 1
            self.down  =  -1
        elif currentColumn == (world.length-1):
            self.left = currentColumn - 1
            self.right = -1
            self.down = currentRow + 1
        else:
            self.left = currentColumn - 1
            self.right = currentColumn + 1
            self.down = currentRow + 1
        
        # perception = [self.left, self.right, self.down]
        # return perception
