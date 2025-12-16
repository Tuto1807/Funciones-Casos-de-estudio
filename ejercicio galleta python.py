#se crea la clase
class Galleta:
    #se crea el metodo constructor
    def _init_(self):
        self.color=" "
        self.forma=" "
        self.tamaño=" "
    #se crea el metodo natural de la clase    
    def asignacion_material(self,dato_color,dato_forma,dato_tamaño):
        self.color=dato_color
        self.forma=dato_forma
        self.tamaño=dato_tamaño
        print(f"las galletas son: (self.color) - de forma: (self.forma) - de tamaño: (self.tamaño)")
        
#***********************codigo principal*****************
#se crea la instancia del objeto
Galleta_chocolate = Galleta()
#se llama el metodo del objeto
Galleta_chocolate.asignacion_material("marron","cuadradas","medianas")
        
#cuando la intancia del objeto tiene argumentos se tiene que utilizar constructor