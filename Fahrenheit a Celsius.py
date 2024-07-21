#Realice un programa que reciba un valor ingresado en temperatura
#en escala Fahrenheit (debe permitir decimales) y lo convierta a su equivalente
#en grados Celsius, luego muestre el resultado.
#La fórmula de conversión que se usa para este cálculo
#es: celsius = (5/9) * (fahrenheit - 32)


fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))

celsius = (5/9) * (fahrenheit - 32)

print("grados en Celsius es:", celsius)