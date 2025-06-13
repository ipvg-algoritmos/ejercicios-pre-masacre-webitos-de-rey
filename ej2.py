cadena_de_texto = (input("Ingrese una frase:"))
vocales = 0
consonantes = 0

for letra in cadena_de_texto:
    if letra.isalpha():
        if letra.lower() in "aeiou":
            vocales = vocales + 1
        else:
            consonantes = consonantes + 1

print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)