from Building import building
from Co2Sensors import co2Sensors
class sheridanSystem:
    def __init__(self, noOfBuild):
        self._noOfBuild = noOfBuild

    def run(self):
        print("Building: " + str(self._noOfBuild) )
       
        buildin = building(int(input('Enter the number of sensors deployed acroos Sheridan Campus: ')),str(input('Enter the building name: ')),
                           int(input('Enter the number of days for sensor(s) to collect CO2 levels: '))
                           )
        buildin.createSenors()
        buildin.printSenInfo()
       


