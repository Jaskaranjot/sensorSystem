from SheridanSystem import sheridanSystem

class application: 
    def start(self):
        letsGo = sheridanSystem(int(input('Enter the number of buildings: ')))
        letsGo.run()

app = application()
app.start()