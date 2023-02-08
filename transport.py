from access_specifiers import Car

car = Car()
print(car.publicVar)
print(car._protectedVar)
print(car.__privateVar)

car.publicMethod()
car._protectedMethod()
car.__privateMetjod()
