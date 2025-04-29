def mostrarLetra(numero):
    for i in range(numero+1):
        print(f"a"*i)

def main():
    num = int(input("Ingresa un numero: "))
    mostrarLetra(num)
    
main()