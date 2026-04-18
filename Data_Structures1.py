list=["Apple", "Banana", "Orange", "Grapes", "Mango"]
print(len(list))
print(list[0])
print(list[-1])

list.append("Pineapple")
print(list)

list.remove("Grapes")
print (list)

list.insert(2, "Strawberry")
print(list)

list.sort()
print(list)

list.pop(0)
print(list)

list.reverse()
print(list)

print("x",list*2)

print(list[:5])

list.clear()
print(list)