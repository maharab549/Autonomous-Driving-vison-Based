
class Servo_PD():
    def __init__(self, servo_p, servo_d):
        self.Kp = servo_p
        self.Kd = servo_d
        self.error = 0
        self.last_error = 0
        self.target = 0
        self.output = 0
        self.output_limit = 3.8

    def calc_servo_pd(self, error):
        self.error = error
        self.output = self.Kp * self.error + self.Kd * (self.error - self.last_error)
        self.last_error = self.error
        if self.output > self.output_limit:
            self.output = self.output_limit
        elif self.output < - self.output_limit:
              self.output = - self.output_limit
        return self.output
