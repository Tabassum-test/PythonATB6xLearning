from abc import ABC, abstractmethod
"""
Whenever we hide bigger classes = Abstraction
Whenever we hide the data variables = Encapsulation
"""
class ExcelReader(ABC):

    @abstractmethod
    def readFromExcal(self):
        pass

class Browser(ExcelReader):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):
    def startBrowser(self):
        print("Starting the Broser")

    def readFromExcal(self):
        print("readfrom excel is ready")

    def runTC(self):
        self.startBrowser()
        self.readFromExcal()
        self.stopBrowser()

tc1 = TC1()
tc1.runTC()
