# time es una libreria que te permite tranajar con funciones de tiempo
import time

# se designa un formato de hora con la libreria 'time' e importa la hora local (del equipo)
tiempo=time.strftime("%H:%M",time.localtime())

# Te pregunta por tu nombre e imprime un saludo segun la hora local
NAME=str(input("Insert your name please: "))
if tiempo < '12':
    print(f"Good morning, {NAME}")
elif tiempo > '12' and tiempo < '21':
    print(f"Good afternoon, {NAME}")
else:
    print(f"Good evening, {NAME}")
    
# if: condicional si, verifica si se cumple una condicion
# elif: entonces si, si la primera condicion no se cumple verifica la segunda
# else: entonces, si ninguna condicion se cumple entrega el mensaje designado