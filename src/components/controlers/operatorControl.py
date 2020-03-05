from wpilib.interfaces import GenericHID


class OperatorControl(GenericHID):
    def __init__(self, id):
        super().__init__(id)
        self.ButtonMap = {"IndexDown": 5, "IndexUp": 6, "Deploy": 1,
                          "PickupOut": 7, "PickupIn": 8}
        self.AxisMap = {}

    def getIndexDown(self) -> bool:
        return self.getRawButton(self.ButtonMap["IndexDown"])

    def getIndexUp(self) -> bool:
        return self.getRawButton(self.ButtonMap["IndexUp"])

    def getPickupDeploy(self) -> bool:
        return self.getRawButtonPressed(self.ButtonMap["Deploy"])

    def getPickupIn(self) -> bool:
        return self.getRawButton(self.ButtonMap["PickupIn"])

    def getPickupOut(self) -> bool:
        return self.getRawButton(self.ButtonMap["PickupOut"])
