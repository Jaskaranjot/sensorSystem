#Parent Class
class ioTSensors:
    def __init__(self, posX, posY, noDays, avgRead):
        self._posX = posX
        self._posY = posY
        self._noDays = noDays
        self._avgRead = avgRead

    def sensoPos(self):
        pass
    def sensorReading(self):
        pass
    def computeAvg(self):
        pass