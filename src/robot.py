from wpilib import TimedRobot, Encoder, run
from networktables import NetworkTables

from components.driveMotor import DriveMotor
from components.driveMotorGroup import DriveMotorGroup
from components.driveBase import DriveBase
from components.solenoid import Solenoid
from components.pressureSensor import PressureSensor
from components.xbox import Xbox
from components.shifter import Shifter


class Robot(TimedRobot):
    def robotInit(self):
        self.right1 = DriveMotor(1, False)
        self.right2 = DriveMotor(2, False)
        self.right3 = DriveMotor(3, False)
        self.right = DriveMotorGroup([self.right1, self.right2, self.right3])

        self.left1 = DriveMotor(4, False)
        self.left2 = DriveMotor(5, False)
        self.left3 = DriveMotor(6, False)
        self.left = DriveMotorGroup([self.left1, self.left2, self.left3])

        #self.testSolenoid = Solenoid(0, 1)
        self.testPressure = PressureSensor(0)
        self.xbox = Xbox(0)
        self.testShifter = Shifter(0, 1, self.xbox)
        

        self.testEncoder = Encoder(1, 2, 3, Encoder.EncodingType.k4X)

        self.dashboard = NetworkTables.getTable("SmartDashboard")

        self.dashboard.putBoolean("Activate", False)

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def teleopInit(self):
        pass

    def testInit(self):
        pass

    def robotPeriodic(self):
        # self.dashboard.putNumber("Velocity", self.right1.getVelocity()/2048*60)
        self.dashboard.putString("Pressure", "{} PSI".format(int(self.testPressure.read())))

        if self.xbox.getShifter():
            print("Should Shift")

    def disabledPeriodic(self):
        pass

    def autonomousPeriodic(self):
        #speed = self.testEncoder.get() / 2048 / 5
        #self.left.set(speed)
        #self.right.set(speed)

        # self.testSolenoid.set(self.dashboard.getBoolean("Activate", False))
        if self.xbox.getShifter():
            print("Should Shift")
        #self.testShifter.update()

    def teleopPeriodic(self):
        self.testShifter.update()

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
