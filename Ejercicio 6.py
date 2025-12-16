#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_uso_cpu():
    uso = float(input("Ingrese el porcentaje de uso de CPU (negativo para terminar): "))
    return uso
def procesar_uso_cpu():
    contador_alertas = 0
    total_mediciones = 0
    mensajes = []
    while True:
        uso = pedir_uso_cpu()
        if uso < 0:
            break
        total_mediciones += 1
        if uso > 90:
            contador_alertas += 1
            mensajes.append("Alerta: Uso Crítico")
    return contador_alertas, total_mediciones, mensajes
def mostrar_resultados(contador_alertas, total_mediciones, mensajes):
    print("Total de mediciones tomadas:", total_mediciones)
    print("Total de alertas críticas:", contador_alertas)
    if mensajes:
        print("Mensajes de alerta:")
        for m in mensajes:
            print(" -", m)
    else:
        print("No se registraron alertas críticas.")
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---      
#-----------------------------
contador_alertas, total_mediciones, mensajes = procesar_uso_cpu()
mostrar_resultados(contador_alertas, total_mediciones, mensajes)