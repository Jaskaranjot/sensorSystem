#Child Class 
import random
from IoTSensors import ioTSensors

class co2Sensors(ioTSensors):
    
    def __init__(self,noDays):

        self._noDays = noDays
        self._sumAvg = 0
        self._co2Levels = []
        
    def sensoPos(self):
        self._posX = random.random() * 100
        self._posY = random.random() * 100

    def sensorReading(self):
        counter = 1
        while counter <= self._noDays:
            self._co2Levels = int(input('Enter the CO2 Reading(PPM) for the day '+str(counter)+': '))
            self._sumAvg += self._co2Levels
            counter += 1
    

    def computeAvg(self):
        avgRead = self._sumAvg / self._noDays
        return avgRead