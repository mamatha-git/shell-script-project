#list
list=["mamatha","chaitra","abhoshek"]
print(list)
print(list[0] + list[1])

print(len(list))

list.append("chaitra")
print(list)

list.remove("chaitra")
print(list)



print(list[0])
print(list[0:3])



#tuples

tuple=("mamatha","chaitra","abhoshek")
print(tuple)
print(tuple[0] + tuple[1])

print(len(tuple))


print(tuple[0])
print(tuple[0:2])

is_present = "mamatha" in tuple #cks if 'apple' is in the tuple (True)

#tuple packing and unpacking
a,b=(8,9)
c,d=a,b
print(c,d)


