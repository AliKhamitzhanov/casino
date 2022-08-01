import random


class Roulette:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def false_argument(self):
        self.user_balance = False
        self.red = False
        self.black = False

    def check_balance(self):
        try:
            if int(user_parlay) <= int(self.balance):
                self.user_balance = True
            else:
                print("У вас не хвответ денег!")
        except ValueError:
            print("Введите число от 0 до 36 или red или black!!!")

    def check(self):
        if self.user_balance:
            try:
                random_number = random.randint(0, 36)
                red_number = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35,)
                for i in red_number:
                    if random_number == i:
                        self.red = True
                black_number = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36)
                for i in black_number:
                    if random_number == i:
                        self.black = True
                user_answer = answer

                if user_answer == "red":
                    if self.red:
                        self.balance -= int(user_parlay)
                        self.balance += int(user_parlay) * 1.5
                        print(f"{self.name} выиграл - х1,5")
                    else:
                        self.balance -= int(user_parlay)
                        print(f"{self.name} проиграл - {user_parlay}")

                elif user_answer == "black":
                    if self.black:
                        self.balance -= int(user_parlay)
                        self.balance += int(user_parlay) * 1.5
                        print(f"{self.name} выиграл - х1,5")
                    else:
                        self.balance -= int(user_parlay)
                        print(f"{self.name} проиграл - {user_parlay}")

                elif random_number == int(user_answer):
                    self.balance -= int(user_parlay)
                    if int(user_answer) == 0:
                        print(f"Please {self.name}")
                        self.balance += int(user_parlay) * 5
                        print(f"{self.name} выиграл - х5")
                    elif int(user_answer) != 0 and int(user_answer) <= 36:
                        self.balance += int(user_parlay) * 3
                        print(f"{self.name} выиграл - х3")

                else:
                    self.balance -= int(user_parlay)
                    print(f"{self.name} проиграл - {user_parlay}")

            except ValueError:
                print("Введите число от 0 до 36 или red или black!!!")

    def info(self):
        print(f"Игрок: {self.name} \n"
              f"Баланс игрока: {self.balance}")


name = input("Как вас зовут?")
user = Roulette(name, 1000)
while True:
    answer = input("Введите число от 0 до 36 или red or black - ")
    user_parlay = input("Сколько вы хотите поставить?")
    user.check_balance()
    user.check()
    user.info()
