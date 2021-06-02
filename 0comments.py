#comments are a great help to summarize certain logics for yourself or other users like below
#Comments can be used to prevent execution when testing code so that the interpreter ignores it
#For multiline comments you can use three """ before opening and after ending places
#The loop is just for example



convert_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * convert_to_units} {name_of_unit}."

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        #we want to do conversion only for positive integers
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
    user_input = input("Hey user, enter the number of days and I will magically convert it to hours!\n")
    validate_and_execute()