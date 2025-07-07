class FirstClass:
    def __init__(self):
        print("This is the First Class"

class SecondClass:
    def __init__(self):
        print("This is the Second Class")
        
    def method(self):
        return "Method in Second Class"


class ThirdClass:
    __slots__ = ()

    def __init__(self):
        print("This is the Third Class")
    @staticmethod
    def another_method():
        return "Method in Third Class"