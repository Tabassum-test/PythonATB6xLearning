from abc import ABC, abstractmethod

class BrowserManager(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop Command")


class ChromeBrowser(BrowserManager):

    def start(selfself):
        #t = ChromeDriver()
        print("we are starting the chrome")

tc = ChromeBrowser()
tc.start()
tc.stop()
