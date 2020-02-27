'''programs showing functions'''
#a function should have a key word def,function name and then brackets()and full colon#
def add():
    sum=5+10
    return sum
#calling a function :add()#
add()
print(add())
def add():
    sum=5+10
    print(sum)
add()
#required argument-you must provide required argument a and b#
def add(a,b):
    sum=a+b
    return sum
print(add(5,10))
print(add(601,720))
print(add(1040,2392))
print(add(12,10))
#default arguments-a default argument b is provided as 10#
def add(a,b=10):
    sum=a+b
    return sum
print (add(120))
def add(a,b=10):
    sum=a+b
    return sum
print (add(120))
#overiding the default #
print(add(120,20))
#arbitrary argument-it uses asteric sign #
def students(*names):
    print("student 1 is" +names[1])
students("john","abdi","mercy")











