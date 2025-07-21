# Author: JOY and IOANNA

class FirstClass:
    __slots__ = ()  # Use slots to reduce memory footprint
    def __init__(self):
        print("This is the First Class")

class SecondClass:
    __slots__ = ()  # Use slots to reduce memory footprint
    def __init__(self):
        print("This is the Second Class")
        
    def method(self):
        return "Method in Second Class"

class ThirdClass:
    __slots__ = ()  # Use slots to reduce memory footprint

    def __init__(self):
        print("This is the Third Class")
    def another_method(self):
        return "Method in Third Class"