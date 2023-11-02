class Car:
    """Represents a car object"""
    miles = 0
    
    # Methods must receive self as first parameter
    def add_miles(self, miles):
        """Increase miles by given number."""
        self.miles += miles

    def display_miles(self):
        """Prints the current miles value."""
        print(f"Current miles: {self.miles}")
                                                      

# We create an instance of Car
astra = Car()
print(astra.miles)

# We can increase the variable within the object, but it's not deal
astra.miles += 50
print(astra.miles)

astra.add_miles(100)
print(astra.miles)

astra.display_miles()
