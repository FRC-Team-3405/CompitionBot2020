from components.solenoid import Solenoid
from components.xbox import Xbox


class Shifter():
    def __init__(self, lowId, highId, xbox: Xbox):
        self.solenoid = Solenoid(lowId, highId)
        self.xbox = xbox
        self.high = False

    def update(self):
        if self.xbox.getShiftUp():
            self.high = True
        elif self.xbox.getShiftDown():
            self.high = False
        
        self.solenoid.set(self.high)
