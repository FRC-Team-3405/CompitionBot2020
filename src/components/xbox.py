from wpilib.interfaces import GenericHID


class Xbox(GenericHID):
    def __init__(self, id):
        super().__init__(id)

    def getLeftX(self) -> float:
        return self.getRawAxis(0)

    def getLeftY(self) -> float:
        return -self.getRawAxis(1)

    def getRightX(self) -> float:
        return self.getRawAxis(3)

    def getRightY(self) -> float:
        return -self.getRawAxis(2)
    
    def getShifter(self) -> bool:
        return self.getRawButtonPressed(6)
 