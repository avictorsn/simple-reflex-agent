'''
Autor: Victor Santiago;
v1.0

'''

import numpy as np
from Environment import Labyrinth
from Actuator import VacuumCleaner
from Sensor import Perception

### Nesta versão, o aspirador tem somente os movimentos de ir para a esquerda, ir para a direta e ir para baixo;

#Environment
length = int(input("Type the dimension of the room to be cleaned: "))
environment = Labyrinth(length)

#Actuators
row = int(input("Type the row position of the Vacuum: "))
column = int(input("Type the column position of the Vacuum: "))
actuator = VacuumCleaner(row, column)

#Sensors
sensor = Perception()


### Programa Agente
print("Simple reflex agent")
print("---------------------------------")
environment.printWorld()
actuator.execute(environment,sensor)