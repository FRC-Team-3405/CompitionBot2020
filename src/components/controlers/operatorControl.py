from wpilib.interfaces import GenericHID


class OperatorControl(GenericHID):
    def __init__(self, id):
        super().__init__(id)
        self.ButtonMap = {"IndexDown": 5, "IndexUp": 6}
        self.AxisMap = {}

    def getIndexDown(self) -> bool:
        return self.getRawButton(self.ButtonMap["IndexDown"])

    def getIndexUp(self) -> bool:
        return self.getRawButton(self.ButtonMap["IndexUp"])
