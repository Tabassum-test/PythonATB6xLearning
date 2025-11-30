class InvalidAgeException(Exception):
    pass

def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking")


can_you_drink(25)
