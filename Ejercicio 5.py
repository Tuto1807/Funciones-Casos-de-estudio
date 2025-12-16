#-------------------------
#------ ZONA CODIGO ------
# ------------------------  
def pedir_producto():
    precio_unitario = float(input("Ingrese el precio unitario del producto (0 para terminar): "))
    if precio_unitario == 0:
        return 0
    cantidad = int(input("Ingrese la cantidad del producto: "))
    return precio_unitario, cantidad
def procesar_compra():
    subtotal = 0
    while True:
        producto = pedir_producto()
        if producto == 0:
            break
        precio_unitario, cantidad = producto
        subtotal += precio_unitario * cantidad
    descuento = 0
    mensaje = "No se aplicó descuento."
    if subtotal > 1000:
        descuento = subtotal * 0.10
        mensaje = "Se aplicó un descuento del 10%."
    elif subtotal > 500:
        descuento = subtotal * 0.05
        mensaje = "Se aplicó un descuento del 5%."
    total_a_pagar = subtotal - descuento
    return total_a_pagar, mensaje
def mostrar_resultados(total_a_pagar, mensaje):
    print("Total a pagar:", total_a_pagar)
    print(mensaje)
#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------
total_a_pagar, mensaje = procesar_compra()
mostrar_resultados(total_a_pagar, mensaje)