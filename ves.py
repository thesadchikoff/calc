from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.YELLOW + 'Весовой калькулятор')
height = float(input('Введите свой рост (см): '))
weight = float(input("Введите свой вес (кг): "))

BMI = float("{0:.2f}".format(weight / ((height / 100) * (height / 100))))

print(f"Ваш текущий ИМТ равен {BMI}")

if(BMI > 40):
    print(Fore.RED + "Ожирение III степени")
elif(BMI >=35):
    print(Fore.RED + "Ожирение II степени")
elif(BMI >=30):
    print(Fore.LIGHTRED_EX + "Ожирение I степени")
elif(BMI >=25):
    print(Fore.LIGHTYELLOW_EX + "Избыточный вес")
elif(BMI >=18.5):
    print(Fore.GREEN + "Нормальный вес")
else:
    print("Недостаточный вес")
        