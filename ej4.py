numeros = []

while True:
    try:
        entrada = float(input("Ingresa un número (número negativo para finalizar): "))
        if entrada < 0:
            break
        numeros.append(entrada)
    except ValueError:
        print("Por favor, ingresa un número válido.")

if numeros:
    promedio = sum(numeros) / len(numeros)
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números válidos.")