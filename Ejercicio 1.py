#-------------------------
#------ ZONA CODIGO ------
# ------------------------

def pedir_pedidos():
        cantidad = int(input("Cuantos pedidos desea realizar: "))
        return cantidad

def procesar(cantidad):
        a = 0
        b = 0
        for i in range(cantidad):
            print("Califique su pedido del 1 al 5 (0 para terminar):")
            try:
                calificacion = int(input())
            except ValueError:
                print("Entrada no válida, se omitirá este pedido.")
                continue

            if calificacion == 0:
                break

            if 1 <= calificacion <= 5:
                if calificacion == 5:
                    print("Calificacion EXCELENTE")
                a = a + calificacion
                b = b + 1
            else:
                print("Calificación inválida. Debe ser entre 0 y 5.")
                continue

        return a, b

def promedio(a, b):
        if b == 0:
            return 0
        promedio = a / b
        return promedio

def resultado(calificacion, cantidad, promedio_val):
        print("El total de puntos son:", calificacion)
        print("El total de pedidos son:", cantidad)
        print("El promedio de calificaciones es:", promedio_val)


#-----------------------------
#---CODIGO PRINCIPAL PYTHON---
#-----------------------------
cantidad = pedir_pedidos()
calificacion, cantidad = procesar(cantidad)
prom = promedio(calificacion, cantidad)
resultado(calificacion, cantidad, prom)