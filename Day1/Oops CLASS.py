# class my_class:
#     def emp(self): #self is repesenting class name (not remove self)
#         print("hello")
#     def disply(self,name):
#         print("Python",name)
#
# obj=my_class()
# obj.emp()
# obj.disply("sahil")

class my_class:
    def emp(self):
        print("hello")
    @staticmethod
    def disply(self,name):# in static method self is parameter
        print("Python",name,self)

obj=my_class()
obj.emp()
obj.disply("hello","sahil")# through object

my_class.disply("hello","sahil")#directly call using class