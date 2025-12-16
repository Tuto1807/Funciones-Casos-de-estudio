#-------------------------
#------ ZONA CODIGO ------
# ------------------------
def pedir_ventas():
    ventas = float(input("Ingrese el monto de ventas del vendedor (0 o negativo para terminar): "))
    return ventas
def procesar_ventas():
    contador_meta_cumplida = 0
    total_vendedores = 0
    mensajes = []
    META = 5000
    while True:
        ventas = pedir_ventas()
        if ventas <= 0:
            break
        total_vendedores += 1
        if ventas >= META:
            contador_meta_cumplida += 1
            mensajes.append("Felicidades: Meta Cumplida")
    return contador_meta_cumplida, total_vendedores, mensajes
def mostrar_resultados(contador_meta_cumplida, total_vendedores, mensajes):
    print("Total de vendedores procesados:", total_vendedores)
    print("Total de vendedores con meta cumplida:", contador_meta_cumplida)
    if mensajes:
        print("Mensajes de felicitación:")
        for m in mensajes:
            print(" -", m)
    else:
        print("Ningún vendedor cumplió la meta.")
        
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------
contador_meta_cumplida, total_vendedores, mensajes = procesar_ventas()

mostrar_resultados(contador_meta_cumplida, total_vendedores, mensajes)
