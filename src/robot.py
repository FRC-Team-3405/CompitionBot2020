from wpilib import TimedRobot, run, Timer
from networktables import NetworkTables

from components.drive.driveMotor import DriveMotor
from components.drive.driveMotorGroup import DriveMotorGroup
from components.drive.driveBase import DriveBase
from components.solenoid import Solenoid
from components.pressureSensor import PressureSensor
from components.controlers.driverControl import DriverControl
from components.controlers.operatorControl import OperatorControl
from components.shifter import Shifter
from components.music import Music
#from components.pickupMotor import PickupMotor
#from components.pickupMotors import PickupMotors
#from components.launcherMotor import LauncherMotor
#from components.indexMotor import IndexMotor
from components.limelight import Limelight
from components.shooter.indexer import Indexer


class Robot(TimedRobot):
    def robotInit(self):
        self.driver = DriverControl(0)
        self.operator = OperatorControl(1)

        self.right1 = DriveMotor(3, True)
        self.right2 = DriveMotor(4, True)
        self.right = DriveMotorGroup([self.right1, self.right2])

        self.left1 = DriveMotor(1, False)
        self.left2 = DriveMotor(2, False)
        self.left = DriveMotorGroup([self.left1, self.left2])

        self.drive = DriveBase(self.right, self.left, self.driver)
        self.driveMotors = [self.right1, self.right2, self.left1, self.left2]
        
        # Most important Part
        self.victoryMusic = Music(self.driveMotors, "victory")
        self.wiiMusic = Music(self.driveMotors, "wii")
        self.zeldaMusic1 = Music(self.driveMotors, "zelda1")
        self.zeldaMusic2 = Music(self.driveMotors, "zelda2")
        self.zeldaMusic3 = Music(self.driveMotors, "zelda3")
        
        #self.pickup1 = PickupMotor(5, False)
        #self.pickup2 = PickupMotor(6, False)
        #self.pickup = PickupMotors([self.pickup1, self.pickup2], self.driver, .5)

        #self.launcher = LauncherMotor(7, self.driver)
        #self.launcher = DriveMotor(7, True)

        #self.indexer = IndexMotor(6, self.driver)
        self.testShifter = Shifter(0, 1, self.driver)

        self.limelight = Limelight(self.drive, self.driver)
        self.dashboard = NetworkTables.getTable("SmartDashboard")
        self.timer = Timer()

        self.indexer = Indexer(self.operator)

    def disabledInit(self):
        pass

    def autonomousInit(self):
        self.wiiMusic.start()
        self.dashboard.putNumber("LauncherSpeed", 0)

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
        delta = self.timer.get()
        self.timer.reset()
        self.indexer.update()
        self.testShifter.update()
        #self.pickup.update()
        #self.indexer.update()
        self.drive.update()
        self.limelight.update()
        self.driver.update()
        #self.launcher.update()
        #self.drive.tankDrive(self.driver.getRightY() ** 3, self.driver.getLeftY() ** 3)

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
