from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBattery(Battery):

    def needs_service(self):
        return (self.current_date - self.last_service_date)>=2

class NubbinBattery(Battery):

    def needs_service(self):
        return (self.current_date - self.last_service_date)>=4