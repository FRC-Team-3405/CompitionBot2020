from wpilib import TimedRobot, run
from networktables import NetworkTables

from components.drive.driveMotor import DriveMotor
from components.drive.driveMotorGroup import DriveMotorGroup
from components.drive.driveBase import DriveBase
from components.controlers.driverControl import DriverControl
from components.controlers.operatorControl import OperatorControl
from components.shifter import Shifter
from components.limelight import Limelight
from components.shooter.indexer import Indexer


class Robot(TimedRobot):
    def robotInit(self):
        self.driver = DriverControl(0)
        self.operator = OperatorControl(1)

        self.dashboard = NetworkTables.getTable("SmartDashboard")

        self.right1 = DriveMotor(3, True)
        self.right2 = DriveMotor(4, True)
        self.right = DriveMotorGroup([self.right1, self.right2])

        self.left1 = DriveMotor(1, False)
        self.left2 = DriveMotor(2, False)
        self.left = DriveMotorGroup([self.left1, self.left2])

        self.drive = DriveBase(self.right, self.left, self.driver)
        self.driveMotors = [self.right1, self.right2, self.left1, self.left2]

        self.shifter = Shifter(0, 1, self.driver)

        self.limelight = Limelight(self.drive, self.driver)

        self.indexer = Indexer(self.operator)

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def teleopInit(self):
        pass

    def testInit(self):
        pass

    def robotPeriodic(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        self.indexer.update()
        self.shifter.update()
        self.drive.update()
        self.limelight.update()

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
