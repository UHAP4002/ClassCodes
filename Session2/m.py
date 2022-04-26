

class Hello:
    def __init__(self, check_login, save):
        self.check_login = check_login

    @staticmethod
    def say_something(what):
        print(what)

    def button_login_pressed(self):
        username = "esmail"
        password = "123"
        if self.check_login(username, password) is True:
            print("Login Successful.")
        else:
            print("Wrong username or password!")


def x():
    pass
