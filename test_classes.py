import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout
# Python doesn't allow imports from filenames starting with numbers
# We need to use the __import__ function
classes_module = __import__("3classes")
FirstClass = classes_module.FirstClass
SecondClass = classes_module.SecondClass
ThirdClass = classes_module.ThirdClass

class TestClasses(unittest.TestCase):
    
    def test_initialization(self):
        """Test that all classes initialize properly."""
        # Capture print output
        output = StringIO()
        with redirect_stdout(output):
            first = FirstClass()
            second = SecondClass()
            third = ThirdClass()
        
        # Check initialization messages
        output_str = output.getvalue()
        self.assertIn("This is the First Class", output_str)
        self.assertIn("This is the Second Class", output_str)
        self.assertIn("This is the Third Class", output_str)
    
    def test_methods(self):
        """Test that class methods work properly."""
        second = SecondClass()
        third = ThirdClass()
        
        self.assertEqual("Method in Second Class", second.method())
        self.assertEqual("Method in Third Class", third.another_method())
    
    def test_attribute_bug_fixed(self):
        """Test that the __slots__ bug has been fixed."""
        first = FirstClass()
        second = SecondClass()
        third = ThirdClass()
        
        # Set and retrieve attributes to verify __slots__ is working properly
        first.name = "TestFirst"
        first.value = 123
        self.assertEqual("TestFirst", first.name)
        self.assertEqual(123, first.value)
        
        second.name = "TestSecond"
        second.category = "Category1"
        self.assertEqual("TestSecond", second.name)
        self.assertEqual("Category1", second.category)
        
        third.name = "TestThird"
        self.assertEqual("TestThird", third.name)
    
    def test_new_methods(self):
        """Test the new methods added to optimize the classes."""
        first = FirstClass()
        second = SecondClass()
        third = ThirdClass()
        
        # Test FirstClass methods
        first.set_data("DataName", "DataValue")
        self.assertEqual(("DataName", "DataValue"), first.get_data())
        
        # Test SecondClass methods
        second.set_category("TestCategory")
        self.assertEqual("TestCategory", second.category)
        
        # Test ThirdClass methods
        third.store_data("key1", "value1")
        self.assertEqual("value1", third.data["key1"])

if __name__ == "__main__":
    unittest.main()
