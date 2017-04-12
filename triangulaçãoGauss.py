'''
    Implementação do Método de Triangulação/Eliminação de Gauss
    link do método passo-a-passo: https://www.youtube.com/watch?v=QFGo3psJltw

    Leonardo Ademir Tonezi dos Santos
    João Ricardo Ito Messias
    Thiago Gonçalvez Costa
'''

mtrz = [[3,-2,5,20],
        [6,-9,12,51],
        [-5,0,2,1]]

def gaussMethod():
    n = 0
    while(n!=2): #Etapas
        print("Etapa :" +str(n+1))
        for linha in range(len(mtrz)):
            if linha>n:
                if mtrz[linha][n] < 0:
                        for coluna in range(len(mtrz)):
                            mtrz[linha][coluna] = mtrz[linha][coluna] * (-1)
                piv = mtrz[linha][n] / mtrz[n][n]
                print ("Pivô da linha " + str(linha) + " : " + str(piv))
            for coluna in range(len(mtrz[0])):
                if coluna>n and linha>n:
                    mtrz[linha][coluna] = round(mtrz[linha][coluna] - (piv * mtrz[n][coluna]))
                elif coluna == n and linha>=n+1:  
                    mtrz[linha][coluna] = round(mtrz[linha][coluna] - (piv * mtrz[n][coluna]))
        print()
        for linha in range(len(mtrz)):
            print(mtrz[linha])

        print()
        n+=1

    print("\nSubstituições: ")
    z = round(mtrz[2][3] / mtrz[2][2])
    y = round((mtrz[1][3] - mtrz[1][2] * z)/mtrz[1][1])
    x = round((mtrz[0][3] - mtrz[0][2] * z - mtrz[0][1] * y)/mtrz[0][0])
    print("x = "+str(x))
    print("y = "+str(y))
    print("z = "+str(z))
    print("Resultado final = "+ str(x),str(y),str(z))

gaussMethod()
