person = {"nome":"Júlia",
"idade":11}
print(person)

print(person["nome"])

person["altura"] = 1.3
print(person)

person["terminouTema"] = True
print(person)

if person["terminouTema"]:
    print(person)

if pessoa["terminouTema"]:
    print("Parabens")
else:
    print("Sem refrigerante")

del person["idade"]
print(person)