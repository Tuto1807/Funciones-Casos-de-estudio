#-------------------------
#------ ZONA CODIGO ------
# ------------------------
def pedir_edad():
    edad = int(input("Ingrese la edad del participante (0 para terminar): "))
    return edad
def procesar_edades():
    publico_objetivo = 0
    suma_edades = 0
    total_participantes = 0
    edad = pedir_edad()
    
    while edad != 0:
        total_participantes += 1
        suma_edades += edad
        if 25 <= edad <= 45:
            publico_objetivo += 1
        print ("Registrado dentro del publico objetivo")
        edad = pedir_edad()
    return publico_objetivo, total_participantes, suma_edades
def mostrar_resultados(publico_objetivo, total_participantes, suma_edades):
    print("Total de participantes registrados:", total_participantes)
    print("Total de participantes dentro del público objetivo (25-45 años):", publico_objetivo)
    if total_participantes > 0:
        promedio_edad = suma_edades / total_participantes
        print("Edad promedio de los participantes:", promedio_edad)
    else:
        print("No se registraron participantes.")
    
    
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------
publico_objetivo, total_participantes, suma_edades = procesar_edades()
mostrar_resultados(publico_objetivo, total_participantes, suma_edades)