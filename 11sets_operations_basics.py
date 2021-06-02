#you cannot access the items in sets like you do in list, but you can use for loop to run them


my_set = {"January", "February", "March"}
for element in my_set:
    print(element)
    
    
my_set.add("April")
print(my_set)

my_set.remove("April")
print(my_set)