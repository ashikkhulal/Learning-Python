#more if elif and else example


convert_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * convert_to_units} {name_of_unit}."
    elif num_of_days == 0:
        print("you entered a 0, please enter a positive number greater than zero")


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
    else:
        print("your input is not a valid number. I cannot proceed forward!")


user_input = input("hey user, enter the number of days and I will convert it to hours!\n")
validate_and_execute()