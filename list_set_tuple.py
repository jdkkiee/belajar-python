# collection = single "Variabel" uset  to store multiple values
# list = [] ordered and changeble. duplicate OK
# set = {} unordered and immutable, but Add/Remove OK
# tuple = () oredered and unchangeble. dublicates OK

fruits = ["Apple", "Orange", "Banana", "Avocado"]

#print(fruits[1])

#for fruit in fruits:
#    print(fruit)

#print(dir(fruits))

#print(help(fruits))

#print(len(fruits))

#print("Pineapple" in fruits)

#fruits[0] = "Pinapple"
#print(fruits[0])

#fruits.append("Pinapple")
#fruits.remove("Apple")
#fruits.insert(0, "Pinapple")
#fruits.sort()
fruits.count("Apple")

for fruit in fruits:
    print(fruit)