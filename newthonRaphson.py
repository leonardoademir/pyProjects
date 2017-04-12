'''
    f  - função f(x)
    g  - função g(x)
    x0 - valor inicial, aleatoriamente escolhido
    e  - precisão
'''
 
def Newton_method(f, g, x0, e):
    n = 0
    x1 = x0 + 10*e
    while abs(x1 - x0) > e:
        print("Iteração : ", n)
        print("x0:",x0)
        x0 = x1
        x1 = x0 - f(x0)/g(x0)      
        print("f(x1) :",f(x1),"\nx1 :", x1,"\n|x1 - x0|: ",round(abs(x1 - x0),6))

        print()
        n+=1
    print("Resultado: ")
    return x1
 
f, g, x0, e = lambda x: 37.104740+3.15122*x-x**2 , lambda x: 3.15122-2*x, 7.86745, 0.0000001

for x in range(-5, 5): #Defino o raio de limite 
    print()
    print(Newton_method(f, g, x, e))


