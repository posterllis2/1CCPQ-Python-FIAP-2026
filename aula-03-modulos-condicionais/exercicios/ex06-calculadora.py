num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

print("[1] Adição")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")

op = int(input("Qual operação você deseja realizar? "))

if op == 1:
    print(f"{num1} + {num2} = {num1+num2}")
else:
    if op == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        if op == 3:
            print(f"{num1} X {num2} = {num1 * num2}")
        else:
            if op == 4:
                print(f"{num1} / {num2} = {num1 / num2}")