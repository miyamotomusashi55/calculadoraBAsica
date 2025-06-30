# Funcion para calcular el factorial
def factorial(numero):
    resultado = 1;
    for i in range(1, numero + 1):
        resultado *= i;

    return resultado;


numero = int(input("Ingrese un numero para calcular su factorial: "));

if(numero > 0):
    resultado = factorial(numero);
    print(f"El factorial del numero {numero} es {resultado}");
else:
    print("El numero no puede ser negativo ni 0.");