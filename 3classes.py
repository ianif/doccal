class FirstClass:
    def __init__(self):
        print("This is the First Class edited by github lalalala")

class SecondClass:
    def __init__(self):
        print("This is the Second Class")
        
    def method(self):
        return "Method in Second Class"

class ThirdClass:
    __slots__ = ()

    def __init__(self):
        print("This is the Third Class")
    def another_method(self):
        return "Method in Third Class"
