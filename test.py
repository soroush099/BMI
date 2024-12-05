from indicatorbmi import Bmi


def main():
    while True:
        question = str(input("Do you want to continue? (yes or no): ").lower().strip())
        if question == "no":
            break

        name = str(input("wat is your name: "))
        age = str(input("Date of birth: "))
        height = str(input("wat is your height in cm: "))
        weight = str(input("wat is your weight in kg: "))
        print(Bmi(name, age, height, weight))


if __name__ == "__main__":
    main()
