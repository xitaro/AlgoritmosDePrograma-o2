from Lista import Lista

lista = Lista()

print("Tamanho da Lista: " + str(lista.tamanho))

lista.adicionar(3)

print("Tamanho da Lista: " + str(lista.tamanho))
lista.imprimir()

valor = input("Digite um valor: ")
lista.adicionar(valor)
print("\n-----------------\n")
lista.imprimir()
print("Tamanho da Lista: " + str(lista.tamanho))

valor = input("Digite um valor que deseja excluir: ")
lista.excluir(valor)
lista.imprimir()
print("Tamanho da Lista: " + str(lista.tamanho))

