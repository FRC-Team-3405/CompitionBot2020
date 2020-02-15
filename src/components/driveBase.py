from .driveMotorGroup import DriveMotorGroup


class DriveBase():
    def __init__(self, right: DriveMotorGroup, left: DriveMotorGroup):
        self.right = right
        self.left = left

    def tankDrive(self, right, left):
        self.right.set(right)
        self.left.set(left)
