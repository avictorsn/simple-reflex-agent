'''
Autor: Victor Santiago;
v1.0

'''

class Labyrinth:
    def __init__(self, length):
        self.length = length
        self.world = [["S" for x in range(length)] for y in range(length)] #inicializando o labirinto
        

    def printWorld(self):
            for i in range(self.length):
                for j in range(self.length):
                    print(self.world[i][j], end="|")
                print()