#Approach 1
# print("Stating point of Program")
# print("Stating point of Program")
# try:
#     print(x)
# except:
#     print("Exception occured")
# print("End point of Program")
# print("end point of Program")

#Appoarch 2

print("hello")
try:
    print(10/0)
except ZeroDivisionError: #you can give exception name
    print("Executed only When Exception Occurd")
else:
    print("Executed only When Exception not Occurd")
finally:
    print("Always Excuted")
print("Program End")