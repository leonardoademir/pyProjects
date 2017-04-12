import math

def gaussMethod():
    n = 0
    for linha in range(len(mtrz)):
        if linha>n:
            if mtrz[linha][n] < 0:
                    for coluna in range(len(mtrz)):
                        mtrz[linha][coluna] = mtrz[linha][coluna] * (-1)
            piv = mtrz[linha][0] / mtrz[0][0]
        for coluna in range(len(mtrz[0])):
            if coluna>n and linha>n:
                mtrz[linha][coluna] = mtrz[linha][coluna] - (piv * mtrz[0][coluna])
            elif coluna == n and linha>=1:  
                mtrz[linha][coluna] = mtrz[linha][coluna] - (piv * mtrz[0][coluna])

    print()

    a = mtrz[1][2] / mtrz[1][1]
    b = (mtrz[0][2] - mtrz[0][1] * a)/mtrz[0][0]

    print("b = "+str(b))
    print("a = "+str(a))
    print()
    if(a < 0):
        print("A função final é g(x) = "+str(b)+" "+str(a)+"x")
    elif(b < 0):
        print("A função final é g(x) = "+str(a)+"x +("+str(b)+")")
    else:
        print("A função final é g(x) = "+str(a)+"x +("+str(b)+")")

    print()
    x = float(input("Digite o valor de x: "))
    print("Com o valor de x = "+str(x)+"\nO resultado da função é: "+str(a*x+b))


#                   Método dos mínimos quadrados

#Matriz de experimentos
mtrzEx = [[0.5, 2, 10, 100, 200],
         [286.5989, 202.656, 135.5243 , 76.21089, 64.08547]]

x = list(map(lambda x: math.log(x), mtrzEx[0]))
print("Experimentos Realizados")
print("Peso = ",mtrzEx[0])
print("Batimento cardíaco = ",mtrzEx[1])
print(x)

#Cálculo do método de mínimos quadrados
n = len(mtrzEx[0])
sumXi = sum(mtrzEx[0])
sumXi2 = sum(list(map(lambda x: x*x, mtrzEx[0])))
sumYi = sum(mtrzEx[1])
sumXiYi = sum(list(map(lambda x,y: x*y, mtrzEx[0], mtrzEx[1])))

#Nova matriz proposta
mtrz = [[n, sumXi,sumYi],
        [sumXi, sumXi2,sumXiYi]]


print()
print("Matriz após aplicado o método")
print(mtrz[0])
print(mtrz[1])

print()
print("Utilizando método de gauss para encontrar variáveis...")
gaussMethod()

