"""
    Simpel test of my github account
"""

class HelloWorld(object):
    # initiate 
    def __init__(self, ground,topping):
        self.ground = ground
        self.topping = topping
    # Just a return method
    def make_a_sandwish(self):
        if self.ground == "Brod":
            return "Make a sandwish: %s on %s" % (self.topping, self.ground)
        else:
            return "Do %s on %s" % (self.topping, self.ground)
    # Overriding __repr__
    def __repr__(self):
        return "Hello world"

#Testrun    
hey = HelloWorld("Brod", "Skinka")
print hey
print hey.make_a_sandwish()


