"""Create a program that asks the user for their weight (in kg) and height (in meters).
Calculate the BMI using the formula:
BMI=height2weight
and display the result with a clear, formatted message, rounded to two decimal places."""

peso=float(input("Digite su peso en Kg: ")) #almacenar el peso en la variable peso
print(f"Su peso es {peso}kg") #mostrar al usuario el peso que ha ingresado

altura=float(input("Digite su altura en metros: ")) #almacenar la altura en la variable altura
print(f"Su altura es {altura}m") #imprimir el valor de la variable altura

imc= peso/(altura**2) #almacenar en la variable imc la formula equivalente a imc

print(f"Su IMC es {imc:.2f}") #imprimir el valor de imc con 2 decimales