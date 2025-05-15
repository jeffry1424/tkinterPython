# Welcome to Python!
# Introducción a Python

# ----------------------------------

# Secuenciales
name = input("Ingrese su nombre: ")                                 # lectura -- input()        
edad = int(input("Ingrese su edad: "))
print("Hola", name, "tienes", edad, "años")                         # escritura -- print()
print("Calculemos el área de un triángulo...")
base = float(input("Ingrese la base del triángulo: "))              # lectura -- input()
altura = float(input("Ingrese la altura del triángulo: "))
area = (base*altura)/2
print("El área del triángulo es", area)                             # escritura -- print()

# ----------------------------------

# Condicionales
print("\n\n\n")
num_1 = float(input("Ingrese un número: "))
num_2 = float(input("Ingrese un número: "))
num_3 = float(input("Ingrese un número: "))

# Determinar y mostrar número mayor
if (num_1 > num_2 and num_1 > num_3) or (num_1 == num_3 and num_1 > num_2):
  print(f"El número mayor es: {num_1}.")
elif (num_2 > num_1 and num_2 > num_3) or (num_2 == num_1 and num_2 > num_3):
  print(f"El número mayor es: {num_2}.")
elif (num_3 > num_1 and num_3 > num_2) or (num_2 == num_3 and num_3 > num_1):
  print(f"El número mayor es: {num_3}.")
elif num_1 == num_2 and num_1 == num_3 and num_2 == num_3:
  print(f"Los tres números son iguales.")

# ----------------------------------

# Ciclos
print("\n\n\n")

# Imprime los primeros n números pares
n = int(input("Ingrese un número: "))
for i in range(0, n*2, 2):
  print(i, end=" ")

# Imprime el promedio de los estudiantes aprobados con un ciclo while (no se sabe la cantidad de estudiantes)
print("\n\n\n")
suma = 0
contador = 0
while True:
  nota = float(input("Ingrese la nota del estudiante (0-10): "))
  if nota < 0 or nota > 10:
    break
  suma += nota
  contador += 1
if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los estudiantes aprobados es: {promedio}.")
else:
    print("No se ingresaron notas válidas.")

# Imprime un menú de opciones que hace operaciones matemáticas con un switch
print("\n\n\n")
opcion = 0
while opcion != 5:
    print("Menú de opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    while opcion < 1 or opcion > 5:
        print("Opción inválida. Ingrese una opción entre 1 y 5.")
        opcion = int(input("Ingrese una opción: "))

    # switch en python
    match opcion:
        case 1:
            num_1 = float(input("Ingrese el primer número: "))
            num_2 = float(input("Ingrese el segundo número: "))
            print(f"La suma es: {num_1 + num_2}.")
        case 2:
            num_1 = float(input("Ingrese el primer número: "))
            num_2 = float(input("Ingrese el segundo número: "))
            print(f"La resta es: {num_1 - num_2}.")
        case 3:
            num_1 = float(input("Ingrese el primer número: "))
            num_2 = float(input("Ingrese el segundo número: "))
            print(f"La multiplicación es: {num_1 * num_2}.")
        case 4:
            num_1 = float(input("Ingrese el primer número: "))
            num_2 = float(input("Ingrese el segundo número: "))
            if num_2 != 0:
                print(f"La división es: {num_1 / num_2}.")
            else:
                print("No se puede dividir entre cero.")
  
print("Fin del programa.")
# ----------------------------------