num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print(f"Os números {num1} e {num2} são múltiplos!")
else:
    print(f"Os números {num1} e {num2} não são múltiplos!")
