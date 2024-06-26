class RemoteTv():

    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        self.volume = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def volumeUp(self):
        if self.volume < 10:
            self.volume += 1

    def volumeDown(self):
        if self.volume > 0:
            self.volume -= 1

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)
        print('Volume is:', self.volume)

# Main code
remoteSatu = RemoteTv()

# Turn switch on, and raise the level 5 times
remoteSatu.turnOn()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.show()

# Lower the level 2 times, and turn switch off
remoteSatu.lowerLevel()
remoteSatu.lowerLevel()
remoteSatu.turnOff()
remoteSatu.volumeDown()
remoteSatu.show()
