#Realice un programa que reciba 2 números enteros diferentes e 
# imprimir el menor de ellos con el mensaje “El menor es: “.

print( "Ingrese 2 numeros enteros diferentes")

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))

while num1 == num2:

    print("Los números debe ser diferentes. Ingrese el segundo número nuevamente.")

if  num1 < num2:
     menor = num1
else:
    menor = num2

print("El menor es:", menor)