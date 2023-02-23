from engine.engine import Engine
from battery import Battery

class Car(Engine, Battery):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()