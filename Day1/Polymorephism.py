# polymorephism = one name multiple form


#Method Overriding
# class Bank:
#     def retOfInterest(self):
#         return 0
# class Xbank(Bank):
#     def retOfInterest(self):
#         return 10
# class Ybank(Bank):
#     def retOfInterest(self):
#         return 12
#
# objx=Xbank()
# print(objx.retOfInterest())#10
#
#
# objy=Ybank()
# print(objy.retOfInterest())#12

# Overloading
class Calculation():
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

objcal=Calculation()
objcal.add()
objcal.add(10,20)
objcal.add(10,21,22)
