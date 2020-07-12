from django.db import models

# Create your models here.


class UserManager(models.Manager):

    def create_user(self, name, password, confirm_password):
        users = User.objects.all()
        password_match = False
        if password == confirm_password:
            password_match = True

        unique_user = True
        for user in users:
            if user.username == name:
                unique_user = False

        if unique_user == True and password_match == True:
            user = self.create(username=name, password=password)
        return unique_user, password_match

    def login_user(self, name, password):
        users = User.objects.all()

        for user in users:
            print(user.username)
            if user.username == name:
                if user.password == password:
                    return "You are now logged in"
                else:
                    return "Password didn't match"

        return "User not found. Please register"


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
