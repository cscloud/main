class Animal:
           """A generic Animal"""
           kind = 'any' # class attribute, shared between instances

           def __init__(self, name): # Initializer, called in object creation
                      self.name = name # instance attribute

class Dog(Animal):
           """A canine thingie"""

           kind = 'k9'

           def speak(self):
                      print '%s says whoof!' % self.name
class Cat(Animal):
           """A feline animal"""

           kind = 'feline'

           def speak(self):
                      print '%s saya meow?' % self.name

           def __len__(self):
                return len(self.name)

            #External string representation

           def __str__(self):
                return 'A cat named %s' % self.name

            # string  representation for developers, usually a way to create such
            # an object

           def __repr__(self):
                return 'Cat(%r)' % self.name
