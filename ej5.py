def procesar_matriz():
    matriz = []

    print("Ingresa los números para una matriz 3x3:")

    for i in range(3):
        fila = []
        for j in range(3):
            num = int(input(f"Ingrese número en posición [{i+1}][{j+1}]: "))
            fila.append(num)
        matriz.append(fila)

    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)

    positivos = 0
    negativos = 0
    ceros = 0
    suma_diag_principal = 0
    suma_diag_secundaria = 0

    for i in range(3):
        for j in range(3):
            valor = matriz[i][j]

            if valor > 0:
                positivos += 1
            elif valor < 0:
                negativos += 1
            else:
                ceros += 1

            if i == j:
                suma_diag_principal += valor
            if i + j == 2:
                suma_diag_secundaria += valor

    print("\nResultados:")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    print(f"Ceros: {ceros}")
    print(f"Suma diagonal principal: {suma_diag_principal}")
    print(f"Suma diagonal secundaria: {suma_diag_secundaria}")

    if suma_diag_principal > suma_diag_secundaria:
        print("La diagonal principal es MAYOR que la secundaria.")
    elif suma_diag_principal < suma_diag_secundaria:
        print("La diagonal principal es MENOR que la secundaria.")
    else:
        print("Ambas diagonales tienen la MISMA suma.")

procesar_matriz()