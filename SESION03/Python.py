''' class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
        mi_clase = Clase ("Que tal")
        mi_clase.atributo_clase
        mi_clase.atributo_instancia
#'Hola'
# #'Que tal' '''
class Clase:
    atributo_clase = "Hola"

    def __init__(self, atributo_instancia): 
        self.atributo_instancia = atributo_instancia

        mi_clase = Clase("Que tal")

        print (mi_clase.atributo_clase)
        print(mi_clase.atributo_instancia)
        
    class Clase:
    atributo_clase= "Hola"
    __atributo_clase="Hola"
def __mi_metodo(self):
    print("Has algo")
    self.__variable=0
    def metodo_normal (self):
        self.__mi_metodo()

        mi_clase = Clase()
        mi_clase.atributo_clase
        mi_clase.metodo_normal()

def es_contraseña_valida(contraseña):
    if len(contraseña) >= 8:
        return True
    else:
        return False

print(es_contraseña_valida("12345678"))  # Imprime True
print(es_contraseña_valida("123"))       # Imprime False

