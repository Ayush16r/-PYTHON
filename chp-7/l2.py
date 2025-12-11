# class MyClass:
#     def __init__(self):
#         self.__private_variable = "this is private variable"
#     def __private_method(self):
#         return " this is private method"
#     def display(self):
#         return f"Accessing private variable: {self.__private_variable}, and private method {self.__private_method()}"


# obj=MyClass()
# #print(obj.__private_variable)
# print("print")
# print(obj.display())



class MyClass:
    def __init__(self):
        self.__public_variable = "this is private variable"
    def __public_method(self):
        return " this is private method"
   


obj=MyClass()
#print(obj.__private_variable)
# print("print")
print(obj.__public_variable)
print(obj.__public_method())