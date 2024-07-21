#Realice un programa que ingrese la edad de una persona y
#la cantidad de artículos comprados en una tienda.
#El programa debe mostrar en pantalla un valor booleano
#(True o False) que indique si la persona es mayor de 18 años de edad y
#además compró más de 1 artículo.

edad = int(input("Ingrese la edad de la persona: "))

cantidad_art = int(input("Ingrese la cantidad de artículos comprados: "))

es_mayor_de_edad = edad > 18
compro_mas_de_un_articulo = cantidad_art > 1
    
resultado = es_mayor_de_edad and compro_mas_de_un_articulo
print(resultado)