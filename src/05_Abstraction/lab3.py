from abc import ABC, abstractmethod

class GearBox(ABC):

    @abstractmethod
    def setGEar(self):
        pass


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Engine, GearBox):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stop")

    def setGEar(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGEar()   # FIXED name
        self.stop()


tesla = Car()
tesla.drive()
