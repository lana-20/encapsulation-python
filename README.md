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
    print(car.publicVar)
    print(car._protectedVar)
    print(car.__privateVar)

    car.publicMethod()
    car._protectedMethod()
    car.__privateMetjod()





