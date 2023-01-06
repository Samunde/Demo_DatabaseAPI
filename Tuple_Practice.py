# 1. Write a Python program to create a tuple.

a=(1,2,3)
print(a)

#2. Write a Python program to create a tuple with different data types.
a=(2,3,7,8) #int Datatype
y=(4)
print(type(y))
b=(2.5,7.89,3.33,2.43)#float Datatype
c=('a','b','c','d')#string Datatype
d=("hello",)#have to give comma to represent tuple
ds=("hello")#this is a string
print(type(ds))
cd=(5+5j,7+2j,54+8j)#complex datatype
print(a)
print(b)
print(c)
print(d)
print(ds)
print(cd)

# 3. Write a Python program to create a tuple with numbers and print one item.

my_tuple=('John','Jennefer','Jack','Paul')
print(my_tuple[2])

# 4. Write a Python program to unpack a tuple in several variables.

a,b,c=(3,4,5)
print(b)

# 5. Write a Python program to add an item in a tuple.

a=input("Enter your tuple")
print(tuple(a))
