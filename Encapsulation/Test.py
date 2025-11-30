class TestExample:

    def __init__(self):  #initializing the instance variables within the constructor
        self.driver = "chrome"        # public variable
        self._config = "STAG"         # protected variable
        self.__api__key = "ABC12345"  # private variable

    def show(self):
        print(f"Driver : {self.driver}")
        print(f"Config : {self._config}")
        print(f"API Key : {self.__api__key}")  # accessible inside class

obj = TestExample()
obj.show()
