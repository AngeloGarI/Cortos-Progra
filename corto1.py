numbers = []
count = 0
print("........Suma de números....")

found = True
while found:
    number = int(input("Ingrese el número: "))

    if number == 0:
        print("Se termina el programa")
        found = False
    else:
        numbers.append(number)
        count += number

print(f"La suma de {numbers} es: {count}")
