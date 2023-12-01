################# EX=1 ###########################

# a=20
# b=30
# c="helloo"
# print(a,b,c)

################# EX=2 ###########################
# in singl variavle store values
# a, b,c = 1,2,"hello"
# print(a,b,c)

################# EX=3 ###########################
# a=100
# b=100
# c=100
# a=b=c=100
# print(a,b,c)

################# EX=4  ###########################
#outside of function are clled as Globalvariable
#inside of function are clled as localvariable

# i,j=10,20 #Globalvariable (Access Eveywhere)
# class my_fun:
#     a,b=100,200  #class variable
#     def dis(self,x,y):
#      print(x+y) #local variable
#      print(self.a+self.b) #class variable
#      print(i+j) #Globalvariable
#
#
# mc=my_fun()
# mc.dis(2,3)

################# EX=5  ########################### (With All Same Name)
a,b=10,20 #Globalvariable (Access Eveywhere)
class my_fun:
    a,b=100,200  #class variable
    def dis(self,a,b):
     print(a+b) #local variable
     print(self.a+self.b) #class variable
     print(globals()["a"]+globals()["b"]) #Globalvariable
