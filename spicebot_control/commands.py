class Command:
    name = ""
    data = []
    is_running = False

    def __init__(self, name):
        self.name = name

    def send(self):
        pass
    
    def setRunning(self):
        self.is_running = True

    def setNotRunning(self):
        self.is_running = False
    
    def getCommandName(self):
        return self.name

    def setData(self ):


        
