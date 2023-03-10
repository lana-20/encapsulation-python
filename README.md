# Encapsulation in Python

Encapsulation (data-hiding) allows to conceal the actual implementation details. This is required to restrict the date from being modified, as data is a crucial part. Data should be prevented from the outside unauthorized access, that's when <code>private</code> access specifiers are used with data. In case I need to access any <code>private</code> data, I should be able to access it with the help of the <code>public</code> functions. 

Create a Python file called <code>access_modifiers.py</code>:

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
    
To call the class, create an ￼ object of this class in a separate file <code>transport.py</code>:

    from access_specifiers import Car

    car = Car()
    
I can access the public variable outside of the class scope.
    
    print(car.publicVar)
    #   Output: Inside Car constructor 9

Python recommends not to access a <code>protected</code> variable by convention (doesn't show it in suggestions), but doesn't restrict it. <code>_protectedVar</code> can ne manually written in and accessed. To follow the proper coding convention/standards, the <code>_protectedVar</code> member shouldn't be accessed outside of the class scope. One can say that the <code>protected</code> access specifier doesn't really exist in Python, as it's not strictly enforced. 

    print(car._protectedVar)
    #   Output: 10

With the <code>private</code> specifier, again, Python does not recommend using it. When manually writing <code>__privateVar</code> in and executing the code, Python throws an error <code>AttributeError: 'Car' object has no attribute '__privateVar'</code>.
    
    print(car.__privateVar)
    #   Output: AttributeError: 'Car' object has no attribute '__privateVar'

I'm not able to access the <code>private</code> variable outside of the class. However, if my intention is still to access it, I can do that using another convention, by prefixing <code>_ClassName</code> to the <code>private</code> variable name.

    print(car._Car__privateVar)
    #   Output: 11

The same case applies to the functions created inside the <code>Car</code> class.

    car.publicMethod()
    #   Output: Calling public method
    
    car._protectedMethod()
    #   Output: Calling protected method
    
    car.__privateMethod()
    #   Output:  AttributeError: 'Car' object has no attribute '__privateMethod'
    
    car._Car__privateMethod()
    #   Output:  Calling private method
    
∴ Encapsulation / data-hiding in Python is implemented via three access specifiers - <code>public</code>, <code>protected</code>, and <code>private</code>.





