convert_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * convert_to_units} {name_of_unit}."
    elif num_of_days == 0:
        print("you entered a 0, please enter a positive number greater than zero")
    else:
        print("you entered an invalid input (only positive numbers greater than zero are allowed)")


user_input = input("hey user, enter the number of days and I will convert it to hours!\n")
user_input_number = int(user_input)


calculated_value = days_to_units(user_input_number)