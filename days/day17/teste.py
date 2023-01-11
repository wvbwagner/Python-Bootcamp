class Car:
    def __init__(self, modelo) -> None:
        self.modelo = modelo
        self.vendor = "FIAT"

celta = Car(modelo='Celta')
celta.vendor = "Chevrolet"

argo = Car('Argo')

class User:

    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('001', 'Wagner')
user_2 = User('002', 'Nubia')

user_1.follow(user_2)

print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
