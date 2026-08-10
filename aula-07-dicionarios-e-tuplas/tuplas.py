# lista de valores *imutáveis* separados por *vírgula*
t = ("a", "b", "c", "d", "e")
print(t)

t1 = "a"
print(t1)

t2 = tuple("fiap")
print(t2)
print(t2[1:3])

# Gambiarra para trocar
t2 = ("F", ) + t2[1:]
print(t2)

# Atribuição com tuplas
a = 5
b = 10
print()
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

email = "fulano@gmail.com"
usuario, dominio = email.split("@")
print()
print(f"usuario: {usuario}, dominio: {dominio}")