from networktables import NetworkTables
from .controlers.driverControl import DriverControl
from .drive.driveBase import DriveBase


class Limelight():
    def __init__(self, driveTrain: DriveBase, driver: DriverControl):
        self.table = NetworkTables.getTable("limelight")
        self.drive = driveTrain
        self.driver = driver
        self.kp = 1

    def update(self):
        if (self.driver.getAim()):
            if (self.table.getNumber("tv", 0) == 1):
                offset = self.table.getNumber("tx")
                self.drive.setRaw(offset*self.kp, -offset*self.kp)

            else:
                self.driver.setRumbleTime(1)
