# Today's project - Quiz Game
import keyword

print("This is a list of Python's keywords", keyword.kwlist)
print()


# 1. Write a declaration, PascalCase
class User:
    # 3. Initialize your object's attributes via a constructor
    def __init__(self, user_id=None, name="Doe"):
        # This is called everytime
        print("A new user has been created.")
        self.user_id = user_id
        self.name = name
        self.time_on_app = 0
        self.friends = 0

    # Methods need a self parameter to keep track of the object that called it

    def app_birthday(self):
        self.time_on_app += 1

    def friend(self, user):
        self.friends += 1
        user.friends += 1


# 2. Create an object, you can add attributes manually OR create a constructor
user_one = User()
print(f"This is a default user:\nID:\t\t{user_one.user_id}\nName:\t{user_one.name}")
user_one.user_id = "001"
user_one.name = "Wanda"

user_two = User("002", "Lwazi")
print(f"\nThis is user one:\nID:\t\t{user_one.user_id}\nName:\t{user_one.name}")
print(f"\nThis is user two:\nID:\t\t{user_two.user_id}\nName:\t{user_two.name}")
