#Realice un programa que reciba un valor en decimales y realice para ese número 
# el cálculo del IVA (15%), muestre en pantalla 
# el valor total que incluya el IVA.

valor = float(input("Ingrese el valor en decimales: "))
iva = valor * 0.15
total = valor + iva
print(f"El valor total con IVA (15%) es: {total}")