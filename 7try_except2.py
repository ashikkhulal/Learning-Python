#you can be more specific with try/except, as you can specify what kind of errors you want to catch


convert_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * convert_to_units} {name_of_unit}."

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a positive number greater than zero")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("your input is not a valid number. i cannot proceed forward!")


user_input = input("hey user, enter the number of days and I will convert it to hours!\n")
validate_and_execute()