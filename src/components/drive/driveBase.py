from .driveMotorGroup import DriveMotorGroup
from ..controlers.driverControl import DriverControl


class DriveBase():
    def __init__(self, right: DriveMotorGroup,
                 left: DriveMotorGroup,
                 driver: DriverControl):
        
        self.right = right
        self.left = left
        self.driver = driver
        self.speed = 1

    def update(self):
        if (self.driver.getSpeedUp()):
            self.speed = 1
        elif (self.driver.getSpeedDown()):
            self.speed = .33
        else:
            self.speed = .66
        left = (self.driver.getLeftY() ** 3) * self.speed
        right = (self.driver.getRightY() ** 3) * self.speed
        self.right.set(right)
        self.left.set(left)
        
    def setRaw(self, right, left):
        self.right.set(right)
        self.left.set(left)
