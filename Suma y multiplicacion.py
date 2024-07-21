#Realice un programa que solicite al usuario dos números
#los sume y muestre el resultadode la suma en pantalla,luego que solicite
#al usuario ingresar un tercer número, 
#el programa debe mostrar en pantalla el resultado


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
        
suma = num1 + num2
print(f"La suma de {num1} y {num2} es: {suma}")

num3 = float(input("Ingrese el tercer número: "))

resultado_final = num3 * suma

print(f"El resultado de multiplicar {num3} por la suma anterior es: {resultado_final}")