from ctre import (TalonFX,
                  SensorCollection,
                  TalonFXControlMode)


class DriveMotor:
    def __init__(self, _id: int, _invert: bool):
        self.motor = TalonFX(_id)
        self.motor.setInverted(_invert)
        self.motor.setSensorPhase(_invert)
        self.sensor = SensorCollection(self.motor)

    def set(self, value: float):
        self.motor.set(TalonFXControlMode.PercentOutput, value)

    def getPostion(self) -> float:
        return self.sensor.getQuadraturePosition()

    def getVelocity(self) -> float:
        return self.sensor.getQuadratureVelocity()
