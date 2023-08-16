#definir clase
class Municipio:
    #declarar atributos de la clase
    nom = ""
    cve = ""
    __pobTot = 0    #variable privada (doble guion bajo)
    _alt = 0        #solo puede ser usada en esta clase, atributos protegidos(guion bajo)
    sup = 0        
    
    # Definir constructor
    def __init__ (self, nombre, clave, pobTotal, altitud, superficie): #Deben de declararse las variables que se ocupan en la clase}
        self.nom = nombre
        self.cve = clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie

    # A todo atributo asimismo a los que sean privado o protegido se le deberá asignar un método GET y SET
    def getNom(self):
        return self.nom
    def setNom(self, nombre):
        try:
            nom = str(nombre)
            self.nom = nombre
        except:
            print("Introduce un municipio")
            
    def getCVE(self):
        return self.cve
    def setCVE(self, clave):
        try:
            cve = str(clave)
            self.cve = clave
        except:
            print("Introduce la clave de un municipio")
            
    def getPOB(self):
        return self.__pobTot
    def setPOB(self, pobTotal):
        try:
            __pobTot = str(pobTotal)
            self.__pobTot = pobTotal
        except:
            print("Introduce la poblacon total de un municipio")
            
    def getALT(self):
        return self._alt
    def setALT(self, altitud):
        try:
            _alt = str(altitud)
            self._alt = altitud
        except:
            print("Introduce la altura de un municipio")
            
    def getSUP(self):
        return self.sup
    def setSUP(self, superficie):
        try:
            sup = str(superficie)
            self.sup = superficie
        except:
            print("Introduce la altura de un municipio")
    
    def info(self):
        print("El nombre del MUNICIPIO es ", self.nom, " con la clave ", self.cve, " con una poblacion de  ", self.__pobTot)
            
            

Mun = Municipio("Toluca", "106", 74515, 4700, 45751)
print(Mun.getNom())           
print(Mun.getCVE())
print(Mun.getPOB())
print(Mun.getALT())
print(Mun.getSUP())


class colonia(Municipio):
    ah = 0
    
    def __init__(self, areaH, nombre, clave, pobTotal, altitud, superficie):
        super().__init__(nombre, clave, pobTotal, altitud, superficie)
        self.ah = areaH
        
    def getAH(self):
        return self.ah
    def setAH(self,ah):
        self.ah= ah
    
    def infoAH(self, value):
        self.ah = self.ah + value
        self.info()
        print (self.nom, "cuenta con ", self.ah, " areas homogeneas. ")
col = colonia(5, "Toluca", "106", 7435435, 4700, 453634)
print(col.infoAH(3))
