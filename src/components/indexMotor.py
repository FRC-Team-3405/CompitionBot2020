from ctre import WPI_VictorSPX, ControlMode


class IndexMotor():
    def __init__(self, id, driver):
        self.motor = WPI_VictorSPX(id)
        self.driver = driver
        self.maxSpeed = .2
    
    def update(self):
        speed = self.maxSpeed if (self.driver.getIndexUp()) else -self.maxSpeed if (self.driver.getIndexDown()) else 0
        self.motor.set(ControlMode.PercentOutput, speed)