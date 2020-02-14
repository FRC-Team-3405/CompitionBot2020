from wpilib import TimedRobot, Encoder, run
from networktables import NetworkTables

from components.driveMotor import DriveMotor
from components.driveMotorGroup import DriveMotorGroup
from components.solenoid import Solenoid
from components.driveBase import DriveBase
from components.xbox import Xbox


class Robot(TimedRobot):
    def robotInit(self):
        self.right1 = DriveMotor(1, False)
        self.right2 = DriveMotor(2, False)
        self.right = DriveMotorGroup([self.right1, self.right2])

        self.left1 = DriveMotor(3, True)
        self.left2 = DriveMotor(4, True)
        self.left = DriveMotorGroup([self.left1, self.left2])

        self.drive = DriveBase(self.right, self.left)

        self.xbox = Xbox(0)

        self.dashboard = NetworkTables.getTable("SmartDashboard")

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def teleopInit(self):
        pass

    def testInit(self):
        pass

    def robotPeriodic(self):
        self.dashboard.putNumber("Velocity", self.right2.getVelocity()/2048*60)

    def disabledPeriodic(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        rightValue = self.xbox.getRightY()
        leftValue = self.xbox.getLeftY()
        self.drive.tankDrive(rightValue, leftValue)

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
