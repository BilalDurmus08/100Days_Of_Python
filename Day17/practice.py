class UserExperience:
    #Pascal Case
    a = 15

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        print("Here constructor")
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


new_user = UserExperience(58, "Bilal")
new_user2 = UserExperience(59, "Yaso Taso")
print(new_user.id)
#for run the class we must use parentheses
new_user.id = "55"
print(new_user.id)

new_user.follow(new_user2)

print(f"{new_user.followers} + {new_user.following} + {new_user2.followers} + {new_user2.following} ")

