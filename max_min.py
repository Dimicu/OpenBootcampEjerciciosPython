num_a=int(input("Escriba un numero"))
num_b=int(input("Escriba otro numero"))

maximo =max(num_a,num_b)
minimo = min(num_a,num_b)

print("El numero mas alto es {} y el numero mas bajo es {}".format(maximo,minimo))

if num_a ==num_b:
    print("Los numero son iguales")