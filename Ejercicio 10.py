#-------------------------
#------ ZONA CODIGO ------
# ------------------------
#El programa solicita el número de horas extra trabajadas por cada empleado. Se debe aplicar una tarifa de bonificación de $15 por hora si las horas extra son mayores a 5. y una tarifa de $10 por hora si son 5 o menos. Se debe acumular el monto total de la bonificación pagada a todos los empleados. Se debe llevar la cuenta de la cantidad de empleados que recibieron bonificación. El proceso termina cuando se ingresa una cantidad de horas negativa.
def pedir_horas_extra():
    horas = int(input("Ingrese el número de horas extra trabajadas por el empleado (negativo para terminar): "))
    return horas
def procesar_empleados():
    total_bonificacion = 0
    contador_empleados_bonificados = 0
    while True:
        horas_extra = pedir_horas_extra()
        if horas_extra < 0:
            break
        if horas_extra > 5:
            bonificacion = horas_extra * 15
        else:
            bonificacion = horas_extra * 10
        if bonificacion > 0:
            contador_empleados_bonificados += 1
        total_bonificacion += bonificacion
    return total_bonificacion, contador_empleados_bonificados
def mostrar_resultados(total_bonificacion, contador_empleados_bonificados):
    print("Total de bonificación pagada a todos los empleados:", total_bonificacion)
    print("Cantidad de empleados que recibieron bonificación:", contador_empleados_bonificados)
    
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

total_bonificacion, contador_empleados_bonificados = procesar_empleados()
mostrar_resultados(total_bonificacion, contador_empleados_bonificados)