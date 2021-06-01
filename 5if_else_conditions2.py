#more if else example


convert_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * convert_to_units} {name_of_unit}."
    else:
        print("You entered an invalid input. (Only positive numbers greater than zero are allowed.)")


user_input = input("Hey user, enter the number of days and I will convert it to hours!\n")


calculated_value = days_to_units(int(user_input))
print(calculated_value)


print(type("this is a class of string"))