                                  # code1
# class MyClass:
#     x = 5
# obj1 = MyClass()
# print(obj1.x)

                                  # code 2
# class Person:
#     def __init__(self,name , age):
#         self.name=name
#         self.age=age
# p1= Person("Ramesh",3)
# print(p1.name)
# print(p1.age)
# p2= Person("Ram",30)
# print(p2.name,p2.age)

                                  # code 3 

# class Person:
#     def __init__(self,name ,):
#         self.name=name
       
#     def greet(self):
#         print("hello, my name is " + self.name)
# p1=Person("ram")
# p1.greet()



# class Calculator:
#     def add(self, a, b):
#         return a+b
    
#     def multiply(self,a,b):
#         return a*b
# calc = Calculator()
# print(calc.add(5,3))
# print(calc.multiply(4,3))


class Playlist:
    def __init__(self , name ):
        self.name=name
        self.songs=[]
    def add_songs(self,songs):
        self.songs.append(songs)
        print(f'added:{song}')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove
    def show_songsk