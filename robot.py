from wpilib import TimedRobot, run, SpeedControllerGroup, Encoder
from wpilib.drive import DifferentialDrive
from networktables import NetworkTables
from ctre import WPI_TalonFX


class Robot(TimedRobot):
    def robotInit(self):
        # Right Motors
        self.RightMotor1 = WPI_TalonFX(1)
        self.RightMotor2 = WPI_TalonFX(2)
        self.RightMotor3 = WPI_TalonFX(3)
        self.rightDriveMotors = SpeedControllerGroup(self.RightMotor1,
                                                     self.RightMotor2,
                                                     self.RightMotor3)
        # Left Motors
        self.LeftMotor1 = WPI_TalonFX(4)
        self.LeftMotor2 = WPI_TalonFX(5)
        self.LeftMotor3 = WPI_TalonFX(6)
        self.leftDriveMotors = SpeedControllerGroup(self.LeftMotor1,
                                                    self.LeftMotor2,
                                                    self.LeftMotor3)
        
        self.drive = DifferentialDrive(self.leftDriveMotors,
                                       self.rightDriveMotors)

        self.testEncoder = Encoder(1, 2, 3)

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
        self.dashboard.putNumber("Encoder", self.testEncoder.getRate())

    def disabledPeriodic(self):
        pass

    def autonomousPeriodic(self):
        self.drive.arcadeDrive(.5, 0)

    def teleopPeriodic(self):
        pass

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
