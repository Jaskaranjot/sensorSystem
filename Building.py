from Co2Sensors import co2Sensors

class building:

    def __init__(self, noOfSensors, buildName, noDays):
        self._noOfSensors = noOfSensors
        self._buildName = buildName
        self._listOfSensors = []
        self._noDays = noDays
    def createSenors(self):
        
        count = 1
        while count <= self._noOfSensors:
            print("Sensor: " ,count)
            sensor = co2Sensors(self._noDays)
            sensor.sensorReading()
            count += 1
    


    def printSenInfo(self):
        print('*********************')
        print("This is for Building: "+ self._buildName)
        print('*********************')
        count = 1
        for sensor in range(self._noOfSensors):
            sensor = co2Sensors(self._noDays)
            sensor.sensoPos()
            self._listOfSensors.append(sensor)
            
        for sensor in self._listOfSensors:
            print("Sensors: ", count)
            count += 1
            print('X: ', round(sensor._posX, 2) )
            print('Y: ', round(sensor._posY, 2) )
            print('Average reading(s): ',round(sensor.computeAvg()), 'PPM')
        

        
           
