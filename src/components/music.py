from ctre import Orchestra


class Music(Orchestra):
    def __init__(self, motors: list):
        super().__init__()
        for i in motors:
            self.addInstrument(i.motor)
        self.loadMusic("/home/lvuser/py/music/victory.chrp")
    
    def victory(self):
        #self.loadMusic("/home/lvuser/py/music/victory.chrp")
        print(self.play())
