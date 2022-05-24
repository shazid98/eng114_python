class Car:

    def __init__(self, current_speed):
        self._maximum_speed = 150
        self.current_speed = current_speed
        if current_speed > self._maximum_speed:
            self.current_speed = self._maximum_speed

    def set_accelerate(self):
        self.current_speed += 10
        if self.current_speed > self._maximum_speed:
            self.current_speed = self._maximum_speed

    def set_brake(self):
        self.current_speed -= 10
        if self.current_speed < 0:
            self.current_speed = 0

    def get_current_speed(self):
        return self.current_speed


tesla = Car(60)

# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()
# tesla.set_accelerate()

# tesla.set_brake()
# tesla.set_brake()
# tesla.set_brake()
# tesla.set_brake()
# tesla.set_brake()
# tesla.set_brake()
# tesla.set_brake()
# tesla.set_brake()

print(tesla.get_current_speed())

