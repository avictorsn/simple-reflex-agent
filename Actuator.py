'''
Autor: Victor Santiago;
v1.0

'''

import time
from Environment import Labyrinth
from Sensor import Perception
import os

class VacuumCleaner:
    
    def __init__(self, rowPosition, columnPosition):
        self.rowPosition = rowPosition      # Posição X atual do agente
        self.columnPosition = columnPosition      # Posição Y atual do agente
        self.clean = False              # O local estará sujo até chegar na posição [tamanho da sala][tamanho da sala]

   
    def execute(self, environment=Labyrinth, perception=Perception): # Execução da limpeza por meio de IA
        print("Let's clean that room! ")
        # Recursivamente executa o processo, sempre tratando os possíveis erros de locomoção do agente
        time.sleep(2)
        clear = lambda: os.system('cls')
        clear()
        print("Agent is in row", self.rowPosition, " and column", self.columnPosition)
        if environment.world[self.rowPosition][self.columnPosition] == "S":
            environment.world[self.rowPosition][self.columnPosition] = "L"
        environment.printWorld()
        perception.capturePerception(environment, self.rowPosition, self.columnPosition) # A cada iteração, o agente atualiza os dados do sensor 
        print("L: ", perception.left, "R: ", perception.right, "D: ", perception.down)
        while not self.clean:
            print("Executing...")  
            time.sleep(2)
            clear = lambda: os.system('cls')
            clear()
            if perception.right != -1:
                if environment.world[self.rowPosition][perception.right] == "S":
                    environment.world[self.rowPosition][perception.right] = "L"
                    self.columnPosition = perception.right
                else:
                    if perception.left != -1:
                        if environment.world[self.rowPosition][perception.left] == "S":
                            environment.world[self.rowPosition][perception.left] = "L"
                            self.columnPosition = perception.left
                        else:
                            if perception.down != -1:
                                if environment.world[perception.down][self.columnPosition] == "S":
                                    environment.world[perception.down][self.columnPosition] = "L"
                                    self.rowPosition = perception.down
                                else:
                                    self.clean = True
                            else:
                                self.clean = True
                    else:
                            if perception.down != -1:
                                if environment.world[perception.down][self.columnPosition] == "S":
                                    environment.world[perception.down][self.columnPosition] = "L"
                                    self.rowPosition = perception.down
                                else:
                                    self.clean = True
                            else:
                                self.clean = True
            else:
                    if perception.left != -1:
                        if environment.world[self.rowPosition][perception.left] == "S":
                            environment.world[self.rowPosition][perception.left] = "L"
                            self.columnPosition = perception.left
                        else:
                            if perception.down != -1:
                                if environment.world[perception.down][self.columnPosition] == "S":
                                    environment.world[perception.down][self.columnPosition] = "L"
                                    self.rowPosition = perception.down
                                else:
                                    self.clean = True
                            else:
                                self.clean = True
                    else:
                            if perception.down != -1:
                                if environment.world[perception.down][self.columnPosition] == "S":
                                    environment.world[perception.down][self.columnPosition] = "L"
                                    self.rowPosition = perception.down
                                else:
                                    self.clean = True
                            else:
                                self.clean = True
            
            print("Agent is in row", self.rowPosition, " and column", self.columnPosition)             
            environment.printWorld()
            perception.capturePerception(environment, self.rowPosition, self.columnPosition) # A cada iteração, o agente atualiza os dados do sensor 
            print("L: ", perception.left, "R: ", perception.right, "D: ", perception.down)
                    
                            

                    

                        