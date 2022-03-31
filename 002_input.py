#input registra informacion generada por teclado

#se solicita tres datos de tipo String (Cadena de texto)
name = input("What is your name?")
colour = input("What is your favorite colour?")
fruit = input("What is your favorite fruit?")

#se imprime una frase con las tres variables.
print(f"{name}, your favorite colour is {colour}, and your favorite fruit is {fruit}")
# nota: al usar 'f' fuera de un String puedes añadir las variables usando '{}',
# con este metodo no es necesario concatenar (+)