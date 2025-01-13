a = (2, 456,45.27,"rohan", True,456, "abhishek")
print(a)

no = a.count(456)
print(no)

i = a.index(45.27)
print(i)

print(len(a))

b=(15,20, 45, 68)
result = a+b
print(result)

print(min(b))
print(max(b))

print(sum(b))
print(20 in b)

#list to touple change-
c=[1,2,3]
d = tuple(c)
print(d)

# assigning the values in a=1,b=2,c=3
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)