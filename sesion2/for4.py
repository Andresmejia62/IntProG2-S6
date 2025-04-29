def tablaMultiplicar (numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Ingrese su numero para mostrar su tabla de multiplicar: "))
    tablaMultiplicar(numero)
    
    main()