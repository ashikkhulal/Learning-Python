#a count down app


from _datetime import datetime

user_input = input("Enter your goal with a deadline, separated by colon (An example input would be learn python: 30.10.2021):\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

date_format = "%d.%m.%Y"
deadline_date = datetime.strptime(deadline, date_format)
today_date = datetime.today()
time_till = deadline_date - today_date

print(f"Dear User! The time remaining for your goal ({goal}) is about {int(time_till.total_seconds() / 60 / 60)} hours.")

