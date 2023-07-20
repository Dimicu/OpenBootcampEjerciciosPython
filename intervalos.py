import random
numero = random.randint(1,120)
print(numero)
if numero in range(10,51):
    print("Está entre 10 y 50")
elif numero in range(51,101):
    print("El numero esta entre 51 y 100")
elif numero in range (101,121):
    print("El numero es mayor de 100")
else :
    print("El numero es menor de 10")