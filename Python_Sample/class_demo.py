class Animal:
           """A generic snimal"""
           kind = 'any' # class attribute, shared between instances

           def __init__(self, name): # Initializer, called in object creation
                      self.name = name # instance attribute
