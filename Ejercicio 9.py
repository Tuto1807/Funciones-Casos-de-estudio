#-------------------------
#------ ZONA CODIGO ------
# ------------------------
#Se comienza con una cantidad inicial en stock (ej. 50 unidades). Se simulan ventas diarias, solicitando la cantidad vendida cada día. Esta cantidad se resta del stock actual. El punto de reposición es de 10 unidades. Después de cada venta, se debe verificar si el stock actual es menor o igual al punto de reposición (condicional). Si es asi, se debe acumular un mensaje de "Aviso de Reposición Urgente" y detener el proceso de ventas.
def pedir_venta():
    cantidad_vendida = int(input("Ingrese la cantidad vendida hoy (0 para terminar): "))
    return cantidad_vendida
def procesar_ventas():
    stock_inicial = 50
    punto_reposicion = 10
    mensajes = []
    while True:
        venta = pedir_venta()
        if venta == 0:
            break
        stock_inicial -= venta
        print(f"Stock actual: {stock_inicial} unidades")
        if stock_inicial <= punto_reposicion:
            mensajes.append("Aviso de Reposición Urgente")
            print("Stock ha alcanzado el punto de reposición. Deteniendo ventas.")
            break
    return stock_inicial, mensajes
def mostrar_resultados(stock_final, mensajes):
    print("Stock final:", stock_final)
    if mensajes:
        print("Mensajes:")
        for m in mensajes:
            print(" -", m)
    else:
        print("No se generaron avisos de reposición.")
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

stock_final, mensajes = procesar_ventas()

