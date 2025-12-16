#-------------------------
#------ ZONA CODIGO ------
# ------------------------
def pedir_transaccion():
    tipo = input("Ingrese el tipo de transacción (D para depósito, R para retiro) o 'FIN' para terminar: ")
    return tipo
def procesar_transacciones():       
    saldo = 1000
    transacciones_validas = 0
    while True:
        tipo = pedir_transaccion()
        if tipo == "FIN":
            break
        monto = float(input("Ingrese el monto de la transacción: "))
        if tipo == "D":
            saldo += monto
            transacciones_validas += 1
            print(f"Depósito realizado. Nuevo saldo: {saldo}")
        elif tipo == "R":
            if saldo - monto >= 0:
                saldo -= monto
                transacciones_validas += 1
                print(f"Retiro realizado. Nuevo saldo: {saldo}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("Tipo de transacción inválido.")  
    return saldo, transacciones_validas
def mostrar_resultados(saldo, transacciones_validas):
    print("Saldo final:", saldo)
    print("Total de transacciones válidas realizadas:", transacciones_validas)
    

#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

saldo, transacciones_validas = procesar_transacciones()
mostrar_resultados(saldo, transacciones_validas)

