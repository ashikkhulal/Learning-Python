#sets are another built-in data type of python, and as with lists, it is used to store multiple items of data. It does not allow duplicate values


convert_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * convert_to_units} {name_of_unit}."

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, which is an invalid input. Please enter a valid input next time")
        else:
            print("You entered a negative number. Please enter a valid input next time")
    except ValueError:
        print("You entered an invalid input. (Your input cannot be texts/ float/ negative numbers.) Please enter a valid input next time")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number or list of days, separated by commas, and I will magically convert it to hours!\n")
    list_of_days = user_input.split(", ")
    
    print(list_of_days)
    print(set(list_of_days))
    
    print(type(list_of_days))
    print(type(set(list_of_days)))
    
    for  num_of_days_element in set(list_of_days):
        validate_and_execute()