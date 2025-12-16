#-------------------------
#------ ZONA CODIGO ------
# ------------------------
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
