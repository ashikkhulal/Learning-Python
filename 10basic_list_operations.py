#Here we create a list, access items from the list, add an item to the list, remove an item from the list and change items in the list


my_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"]
print(my_list[2])
my_list.append("December")
print(my_list[7])

def list_of_months():
    print("The 12 months of a year are: ")
    print(*my_list, sep = "\n")
    

list_of_months()