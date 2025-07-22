# Author: JOY and IOANNA
"""
Module containing three classes with optimized memory usage.
"""

class FirstClass:
    """Base class that demonstrates the use of __slots__ for memory optimization."""
    __slots__ = ('name', 'value')  # Define attributes that can be stored
    
    def __init__(self):
        """Initialize the FirstClass instance and print a message."""
        print("This is the First Class")
        self.name = None
        self.value = None
    
    def set_data(self, name, value):
        """Set the name and value attributes.
        
        Args:
            name: The name to set
            value: The value to set
        """
        self.name = name
        self.value = value
    
    def get_data(self):
        """Get the name and value as a tuple.
        
        Returns:
            tuple: (name, value)
        """
        return (self.name, self.value)

class SecondClass:
    """Class that extends functionality with a specific method."""
    __slots__ = ('name', 'category')  # Define attributes that can be stored
    
    def __init__(self):
        """Initialize the SecondClass instance and print a message."""
        print("This is the Second Class")
        self.name = None
        self.category = None
        
    def method(self):
        """A method specific to SecondClass.
        
        Returns:
            str: A string indicating this is a method in SecondClass
        """
        return "Method in Second Class"
    
    def set_category(self, category):
        """Set the category attribute.
        
        Args:
            category: The category to set
        """
        self.category = category

class ThirdClass:
    """Class with additional methods and attributes."""
    __slots__ = ('name', 'data')  # Define attributes that can be stored

    def __init__(self):
        """Initialize the ThirdClass instance and print a message."""
        print("This is the Third Class")
        self.name = None
        self.data = {}
        
    def another_method(self):
        """Another method specific to ThirdClass.
        
        Returns:
            str: A string indicating this is a method in ThirdClass
        """
        return "Method in Third Class"
    
    def store_data(self, key, value):
        """Store data in the data dictionary.
        
        Args:
            key: The key to use
            value: The value to store
        """
        self.data[key] = value
