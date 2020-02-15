from components.solenoid import Solenoid
from components.xbox import Xbox


class Shifter():
    def __init__(self, lowId, highId, xbox: Xbox):
        self.solenoid = Solenoid(lowId, highId)
        self.xbox = xbox
        print(self.xbox)
        self.high = False

    def update(self):
        if self.xbox.getShifter():
            print("pressed")
            self.high = not self.high
        
        self.solenoid.set(self.high)
