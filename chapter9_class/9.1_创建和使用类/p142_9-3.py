class User():
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def describe_user(self):
        print('Your first name is ' + self.first.title())
        print('Your last name is ' + self.last.title())

    def greet_user(self):
        print('Hello! ' + self.first.title() + ' ' + self.last.title())


my_user = User('zhang', 'chen')
my_user.greet_user()
my_user.describe_user()

user = User('zhang', 'wei')
user.greet_user()
user.describe_user()