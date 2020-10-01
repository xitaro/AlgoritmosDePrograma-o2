#Construa um algoritmo que possua uma tupla com os números escritos por extenso de “zero” a “nove”.
#Peça ao usuário para digitar um nome de 0 a 9 e retorne a ele o número por extenso,
#sem usar estruturas condicionais (if e switch).

#create tuple
stringNumbers = ("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove")

choose = int(input("Digite um número de zero a nove: "))

print(stringNumbers[choose])

#Construa um algoritmo que peça ao usuário para informar o nome, a nota01 e a nota02 de um aluno.
#Guarde estas informações em um dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
# e adicione ao dicionário. Ao final, imprima todos os dados do dicionário.
user = {}

user["name"] = input("Informe seu nome: ")
user["note01"] = int(input("Informe sua nota: "))
user["note02"] = int(input("Informe a sua segunda nota: "))
user["finalNote"] = (user["note01"] + user["note02"])/2

print(user)