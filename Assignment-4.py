print("create and access dictionary elements")
my_dict={"Name":"Alice",'Age':29,"City":"New York"}
print("created dictionary:",my_dict)
print("access 'name':",my_dict["Name"])
print("access 'age':",my_dict["Age"])
print("\n update dictionary")
my_dict["City"]="San Diego"
print("updated dictionary:",my_dict)
my_dict["profession"]="astronaut"
print("added 'profession':",my_dict)
print("\n removing elements")
remove_dict=my_dict.pop("Age")
print("removed single element 'Age':",my_dict)
del my_dict["Name"]
print("deleted key value pair in dictionary:",my_dict)
my_dict.clear()
print("Removed all elements in dictionary:",my_dict)