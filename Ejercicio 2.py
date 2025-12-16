#-------------------------
#------ ZONA CODIGO ------
# ------------------------
def pedir_codigo():
    codigo = input("Ingrese el codigo de acceso de entrada.")
    return codigo
def procesar_accesso(codigo):
    codigo_correcto = "1807"
    permitidos = 0
    denegados = 0
    while True:
        codigo = pedir_codigo()
        if codigo == "salir":
            break
        if validar_codigo(codigo, codigo_correcto):
            print("Acceso Permitido")
            permitidos += 1
        else:
            print("Acceso Denegado")
            denegados += 1
        return permitidos, denegados
def validar_codigo(codigo, codigo_correcto):
    if codigo == codigo_correcto:
        return True
    else:
        return False
def mostrar_resultados(permitidos, denegados):
    print("Total de accesos permitidos:", permitidos)
    print("Total de accesos denegados:", denegados)



#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------

permitidos, denegados = procesar_accesso("")
mostrar_resultados(permitidos, denegados)