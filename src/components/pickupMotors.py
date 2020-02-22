from .pickupMotor import PickupMotor
from .xbox import Xbox
from typing import List


class PickupMotors():
    def __init__(self, _motors: List[PickupMotor],
                 _xbox: Xbox, _maxOutput: int):

        self.motors = _motors
        self.xbox = _xbox
        self.maxOutput = _maxOutput

    def update(self):
        if self.xbox.getPickupForward():
            for i in self.motors:
                i.set(self.maxOutput)
        elif self.xbox.getPickupBackward():
            for i in self.motors:
                i.set(-self.maxOutput)
        else:
            for i in self.motors:
                i.set(0)
            
