
def bisiesto(y):
    bisies = False
    if y % 4 ==0 and y % 100 !=0:
        bisies=True
    elif y % 4==0 and y % 100 ==0 and y % 400 ==0:
        bisies=True
    else:
        bisies=False

    return bisies
        
def textoBis(x):
    if x == True:
        print("{} es un año bisiesto".format(ano))
    else:
        print("{} NO es un año bisiesto".format(ano))
        
ano = int(input("Escribe un año: "))
bisiesto(ano)
resultadoano = bisiesto(ano)
textoBis(resultadoano)