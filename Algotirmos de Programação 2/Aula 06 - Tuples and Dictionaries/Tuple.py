#create tuple
cars = ("Uno", "Doblo", "Toro")
#print tuple in position 1
print(cars[1])

#print all values in the tuple
for car in cars:
        print(car)
#print between
print(car[1:2])
#ordenado
print(sorted(cars))
print(cars)
#for com range
for car in range(len(cars)-2):
    print ("Posição"+str(car)+": "+cars[car])

#calcular
def calcular(x,y):
    return(x+y),(x-y),(x*y),(x/y)

print(calcular())