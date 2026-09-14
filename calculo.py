print("ingresar tiempo(minutos)")
tiempo=float(input())
print("ingresar objeto adquirido durate el plazo")
objeto=float(input())
hora=(objeto/tiempo)*60
print("obtienes",objeto/tiempo,"cada minuto,",hora," cada hora")
plazo=0
print("calcular por un plazo de tiempo(A) o para conseguir una cantidad del objeto especifica(B)(presionar otra tecla para cerrar)?")
decision=input()
if decision == "A":
    print("insertar plazo(usar minutos)")
    plazo=float(input())
    print("obtienes",(objeto/tiempo)*plazo,"por",plazo,"minutos,",(objeto/tiempo)*plazo*60,"a la hora")
elif decision == "B":
    print("insertar cantidad del objeto que deseas conseguir")
    cantidad=float(input())
    print("necesitas",cantidad/(objeto/tiempo),"minutos para conseguir",cantidad,"del objeto,",(cantidad/(objeto/tiempo))/60,"horas")
else:
    print("cerrando el programa")