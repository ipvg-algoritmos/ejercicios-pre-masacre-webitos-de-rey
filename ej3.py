def encontrar_max_min_usuario():
    numeros_ingresados = []

    print("Por favor, ingresa números. Para finalizar la lista, escribe un número negativo.")

    while True:
        try:
            entrada = input("Ingresa un número: ")
            numero = int(entrada)

            if numero < 0:
                break
            else:
                numeros_ingresados.append(numero)

        except ValueError:
            print("tonto eso no es un número entero. Por favor, intentalo de nuevo.")
            continue

    if not numeros_ingresados:
        print("No ingresaste ningún número válido en la lista.")
    else:
        valor_mas_alto = max(numeros_ingresados)
        valor_mas_bajo = min(numeros_ingresados)

        print(f"De los números que ingresaste:")
        print(f"El valor *más alto* es: {valor_mas_alto}")
        print(f"El valor *más bajo* es: {valor_mas_bajo}")

encontrar_max_min_usuario()