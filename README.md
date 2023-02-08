# encapsulation-python

Create a Python file called access_modifiers.py:

    class Car:
      publicVar = 9
      _protectedVar = 10
      __privateVar = 11

      def __init__(self):
        print("Inside Car constructor")

      def publicMethod(self):
        print("Calling public method")

      def _protectedMethod(self):
        print("Calling protected method")

      def __privateMethod(self):
        print("Calling private method")
    
To call the class, create an object of this class in a separate file transport.py:

    from access_specifiers import Car

    car = Car()
    
Can access the public variable outside of the class scope.
    
    print(car.publicVar)
    #   Output: Inside Car constructor 9

Python suggests not to access a protected variable by convention, but doesn't restrict it. _protectedVar can ne manually written in and accessed. To follow the proper coding convention/standards, the _protectedVar member shouldn't be accessed outside of the class scope. One can say that the <code>protected</code> access specifier doesn't really exist in Python, as it's not strictly enforced. 

    print(car._protectedVar)
    #   Output: 10

    print(car.__privateVar) #

    car.publicMethod()
    car._protectedMethod()
    car.__privateMetjod()





