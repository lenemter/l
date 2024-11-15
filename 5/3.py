class Car:
    def __init__(self, wheels, doors) -> None:
        self.wheels = wheels
        self.doors = doors

        self.is_started = False
    
    def speak(self):
        print("Boom")
    
    def start(self):
        self.is_started = True
