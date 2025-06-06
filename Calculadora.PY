def calculadora():
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    operacion = input("Elige una operación (1/2/3/4): ")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == "1":
        print("Resultado:", num1 + num2)
    elif operacion == "2":
        print("Resultado:", num1 - num2)
    elif operacion == "3":
        print("Resultado:", num1 * num2)
    elif operacion == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: No se puede dividir por cero")
    else:
        print("Operación no válida")

calculadora()
# Este código es una calculadora simple que permite al usuario realizar operaciones básicas
# de suma, resta, multiplicación y división. El usuario elige la operación y proporciona dos números
