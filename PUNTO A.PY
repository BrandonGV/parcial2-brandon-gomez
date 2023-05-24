print("Bienvenido a la secuencia del cuadrado de los numeros")

def mostrar_cuadrados(n):
    suma = 0
    for i in range(1, n+1):
        cuadrado = i*i
        suma += 2*i - 1
        
        print(f"El cuadrado de {i} es {cuadrado} se halla con la operación {cuadrado} =", end=" ")
        
        for j in range(1, i+1):
            termino = 2*j - 1
            if j == i:
                print(f"{termino}", end="")
            else:
                print(f"{termino} + ", end="")
        
        print(f" = {suma}")
n = int(input("cuantos valores quieres?: "))
print(mostrar_cuadrados(n))