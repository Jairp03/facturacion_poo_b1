class Company:
    next = 0  # Variable de clase(estatica) para almacenar el próximo ID disponible
    # meetodo constructor que s eejecuta cuando se instancia la clase
    def __init__(self, name="Melissa", ruc="0943213456001"):
        # Incrementa el contador de ID para cada nueva instancia
        Company.next += 1
        # variables de instancias
        self.__id = Company.next  # Asigna el ID único a la instancia actual privada
        self.business_name = name  # Asigna el razon social de la empresa a la instancia actual
        self.ruc = ruc  # Asigna el RUC de la empresa a la instancia actual
        
    # metodo de usuraio que muestra la información de la empresa (ID, nombre y RUC)
    def show(self):
        print(f"Id:{self.__id} Empresa: {self.business_name} ruc:{self.ruc}")

if __name__ == '__main__':
    # Se ejecuta solo si este script es el principal
    print("***********************************************************")
    # Crea dos instancias(objetos) de la clase Company con nombres diferentes
    comp1 = Company("SuperMaxi")
    comp2 = Company(ruc="9999999999001")
    # Muestra la información de la primera empresa
    comp1.show()
    print("-----------------------------------------------------------")
    # Muestra la información de la segunda empresa
    comp2.show()
    print("-----------------------------------------------------------")
    # print(comp2.__id)
    print(Company.next)
    
