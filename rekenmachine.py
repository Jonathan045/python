
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Kies een optie.")
print("1.+")
print("2.-")
print("3.*")
print("4./")

while True:

    choice = input("Maak een keuze tussen(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Voer eerste nummer in: "))
        num2 = float(input("Voer tweede nummer in: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        

        next_calculation = input("Nog een keer? (Ja/Nee): ")
        if next_calculation == "nee":
          break
    
    else:
        print("Invalid Input")