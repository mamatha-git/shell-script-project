#example
dict={
    "name":"mamatha",
    "age":44,
}
print(dict)
print(type(dict))

print(dict.get("salary","not found"))  # to avoid the error 

dict["name"]="sahana" #modifing
print(dict)
dict["company"]="amazon" # adding the key value pair
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())