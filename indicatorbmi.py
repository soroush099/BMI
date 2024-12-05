import datetime


class Bmi:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.height2 = None
        self.bmi = None
        self.bol = True
        self.indicator = None

    def change(self):

        self.height2 = int(self.height) / 100
        self.weight = float(self.weight)

    def agey(self):
        try:
            day, mons, year = self.age.split("/")
            year, mons, day = int(year), int(mons), int(day)

            if 1 > day > 31 or 1 > mons > 12 or 0 > year:
                self.bol = False

        except ValueError:
            self.bol = False

    def save_as_file(self):
        with open("bmii.txt", "a") as file:
            file.write(
                f"name: {self.name}\n"
                f"age: {self.age}\n"
                f"height: {self.height}cm\n"
                f"weight: {self.weight}kg\n"
                f"BMI: {self.bmi:.2f}\n"
                f"Time: {datetime.datetime.today():%d/%m/%Y}\n"
                f"Indicator: {self.indicator}\n \n"
            )

    def mohasebe(self):
        try:
            self.change()
            self.bmi = self.weight / (self.height2 ** 2)

            if self.bmi < 16:
                self.indicator = "Severe Underweight"
            elif 16 <= self.bmi <= 18.5:
                self.indicator = "Underweight"
            elif 18.5 < self.bmi <= 25:
                self.indicator = "Normal"
            elif 25 < self.bmi <= 30:
                self.indicator = "Overweight"
            elif 30 < self.bmi <= 35:
                self.indicator = "Class 1 Obesity"
            elif 35 < self.bmi <= 40:
                self.indicator = "Class 2 Obesity"
            else:
                self.indicator = "Class 3 Obesity"
        except ValueError:
            self.bol = False

    def __str__(self):
        self.agey()
        self.mohasebe()

        if self.bol == True and self.name != "":
            a = (
                f"name: {self.name}\n"
                f"BMI: {self.bmi:.2f}\n"
                f"Indicator: {self.indicator}\n"
            )
            self.save_as_file()
            return a
        else:
            return "invalid"
