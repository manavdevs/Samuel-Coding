my_dict = {}
my_dict = {1:"apple", 2:"banana", 3:"cherry"}

my_dict={"name":"Samuel", "age":12, "city":"Markham",1:[1,2,3]}

print(my_dict["name"])
print (my_dict.get("age"))

my_dict["age"]=12
print(my_dict)
      
my_dict["country"]="Canada"
print(my_dict)
my_dict.pop("city")
print(my_dict)

my_dict.clear()
print(my_dict)