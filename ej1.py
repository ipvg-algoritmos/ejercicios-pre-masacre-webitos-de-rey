numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La lista de números es {numeros}")
numero_usuario = int(input("Inserta un número a buscar: "))
for i in range(len(numeros)):
    if numeros[i] == numero_usuario:
        print("Tu número está en la lista y en la posición:", i)
        break
else:
    print("Tu número no está en la lista")