#-------------------------
#------ ZONA CODIGO ------
# ------------------------
def pedir_unidades():
    unidades = int (input("Ingrese la cantidade de unidades producidas en el lote (0 para terminar):"))
    return unidades
def procesar_unidad(numero):
    estado = input(f"unidad {numero}: ¿Es defectuosa? (s/n): ").upper()
    return estado == 'S'
def mostrar_resultados(total_lotes, total_defectuosas):
    print("Total de lotes procesados:", total_lotes)
    print("Total de unidades defectuosas:", total_defectuosas)
    print("total de unidades buenas:", total_unidades - total_defectuosas)

#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------
total_unidades = pedir_unidades()

if total_unidades == 0:
    print("No se procesaron lotes.")
else:
    defectuosas = 0
    
    for i in range(1, total_unidades + 1):
        if procesar_unidad(i):
            defectuosas += 1

mostrar_resultados(total_unidades, defectuosas)