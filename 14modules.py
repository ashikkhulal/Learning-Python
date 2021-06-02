#dictionaries are used to store values in key:value pair. It is a collection, which does not allow duplicate values.


def days_to_units(num_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{num_of_days} days are {num_of_days * 24} hours."
        elif conversion_unit == "minutes":
            return f"{num_of_days} days are {num_of_days * 24 * 60} minutes."
        elif conversion_unit == "seconds":
            return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds."
        else:
            return "unsupported unit. units can only be either hours, minutes or seconds."

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, which is an invalid input. Please enter a valid input next time")
        else:
            print("You entered a negative number. Please enter a valid input next time")
    except ValueError:
        print("You entered an invalid input. (Your input cannot be texts/ float/ negative numbers.) Please enter a valid input next time")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit, separated by colon(:)!\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print("You entered: ")
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
    