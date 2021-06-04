# creating a class for user
# we also have a constructor
# functions that belong to a class are called methods

class User:
    def __init__(self, name, email, password, current_job_title):
        self.name = name
        self.email = email
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. And you can contact them at {self.email}")


app_user_one = User("Ashik Khulal", "aa@aa.com", "1234", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("DevOps Lead")
app_user_one.get_user_info()

app_user_two = User("James Bond", "bb@bb.com", "supersecret", "Super Agent")
app_user_two.get_user_info()
