from wpilib import TimedRobot, Encoder, run
from networktables import NetworkTables

from components.driveMotor import DriveMotor
from components.driveMotorGroup import DriveMotorGroup
from components.driveBase import DriveBase
from components.solenoid import Solenoid
from components.pressureSensor import PressureSensor
from components.xbox import Xbox
from components.shifter import Shifter
from components.music import Music
from components.pickupMotor import PickupMotor
from components.pickupMotors import PickupMotors


class Robot(TimedRobot):
    def robotInit(self):
        self.xbox = Xbox(0)

        self.right1 = DriveMotor(1, True)
        self.right2 = DriveMotor(2, True)
        self.right = DriveMotorGroup([self.right1, self.right2])

        self.left1 = DriveMotor(3, False)
        self.left2 = DriveMotor(4, False)
        self.left = DriveMotorGroup([self.left1, self.left2])

        self.drive = DriveBase(self.right, self.left)
        self.driveMotors = [self.right1, self.right2, self.left1, self.left2]
        
        # Most important Part
        self.victoryMusic = Music(self.driveMotors, "victory")
        self.wiiMusic = Music(self.driveMotors, "wii")
        self.zeldaMusic1 = Music(self.driveMotors, "zelda1")
        self.zeldaMusic2 = Music(self.driveMotors, "zelda2")
        self.zeldaMusic3 = Music(self.driveMotors, "zelda3")
        
        self.pickup1 = PickupMotor(5, False)
        self.pickup2 = PickupMotor(6, False)
        self.pickup = PickupMotors([self.pickup1, self.pickup2], self.xbox, .5)
        self.testShifter = Shifter(0, 1, self.xbox)

        self.dashboard = NetworkTables.getTable("SmartDashboard")

    def disabledInit(self):
        pass

    def autonomousInit(self):
        self.zeldaMusic3.start()

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
        self.testShifter.update()
        self.pickup.update()
        self.drive.tankDrive(self.xbox.getRightY()/4, self.xbox.getLeftY()/4)

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
