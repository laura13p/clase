class Municipio:
    
    nom = ""
    cve = ""
    __pobTot = 0 # se define con doble guion bajo como una propiedad privada 
    _alt = 0     # cuando tiene solo un guion bajo solo se puede utilizar es esta clase 
    sup = 0
    #definir constructor
    def __init__ (self, nombre, clave, pobTotal, altitud, superficie):
        self.nom = nombre
        self.cve = clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie
    # A todo atributo que sea privado o protegido se le deberá asignar un metodo GET Y SET
    def getNom(self):
        return self.nom
    def setNom(self, nombre):
        try:
            nom = str (nombre)
            self.nom = nombre
        except:
            print("Introduce un Municipio")
            
Mun = Municipio("Toluca", "106", 7435435, 4700, 453634)
print ( Mun.getNom())
            
            