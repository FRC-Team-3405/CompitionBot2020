from wpilib.interfaces import GenericHID


class Xbox(GenericHID):
    def __init__(self, id):
        super().__init__(id)
        self.ButtonMap = {"ShiftUp": 10, "ShiftDown": 9, "PickupForward": 6, "PickupBackward": 5}
        self.AxisMap = {"RightY": 5, "RightX": 4, "LeftY": 1, "LeftX": 0}

    def getLeftX(self) -> float:
        return self.getRawAxis(self.AxisMap["LeftX"])

    def getLeftY(self) -> float:
        return -self.getRawAxis(self.AxisMap["LeftY"])

    def getRightX(self) -> float:
        return self.getRawAxis(self.AxisMap["RightX"])

    def getRightY(self) -> float:
        return -self.getRawAxis(self.AxisMap["RightY"])

    def getShiftUp(self) -> bool:
        return self.getRawButton(self.ButtonMap["ShiftUp"])

    def getShiftDown(self) -> bool:
        return self.getRawButton(self.ButtonMap["ShiftDown"])

    def getPickupForward(self) -> bool:
        return self.getRawButton(self.ButtonMap["PickupForward"])

    def getPickupBackward(self) -> bool:
        return self.getRawButton(self.ButtonMap["PickupBackward"])
