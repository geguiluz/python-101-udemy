class Car:
    """Represents a car object"""
    miles = 0
    
    def __init__(self, color, make, model, miles=0):
        """Set initial details of car."""
        self.color = color
        self.make = make
        self.model = model
        self.miles = miles

    # Methods must receive self as first parameter
    def add_miles(self, miles):
        """Increase miles by given number."""
        self.miles += miles

    def display_miles(self):
        """Prints the current miles value."""
        print(f"Current miles: {self.miles}")
                                                      

# We create an instance of Car
astra = Car("Red", "Vauxhall", "Astra")
print(astra.miles)

# We can increase the variable within the object, but it's not deal
astra.miles += 50
print(astra.miles)

astra.add_miles(100)
print(astra.miles)

astra.display_miles()

prius = Car("Blue", "Toyota", "Prius", 1000)
prius.display_miles()
prius.add_miles(50)
prius.display_miles()
