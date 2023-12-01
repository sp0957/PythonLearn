# class my_class:
#     def __init__(self): #fix syntax for constrctor def __init__(self):
#         print("This is constructor")
#     def me(self):
#         print("This is Method")
#
# mc=my_class() #invok constructor Automatically
# mc.me()       #method call by using object

# class my_class:
#     name="sahil"
#     def __init__(self,name): #fix syntax for constrctor def __init__(self):
#         print(name)
#         print(self.name)
#
# mc=my_class("Jenish")# PAss parameter to the constructor


class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid, self.ename, self.sal)

e1=Emp(1,"sahil",1000000)
e1.display()