class MyClass:
    def __init__(self):
        self._public_variable = "this is private variable"
    def _public_method(self):
        return " this is private method"
   


obj=MyClass()
#print(obj.__private_variable)
# print("print")
print(obj._public_variable)
print(obj._public_method())