from cargo import Cargo

Class Empleado:
      secuencia= 0
      def__init__(self,nom="",sue0,car=None):
          self.codigo=self.generarCodigo()
          self.nombre=nom 
          self.sueldo=sue 
          self.cargadorEmp=car 
          
          def generarCodigo(self):
              Empleado.secuencia=Empleado.secuencia+1
              return Empleado.secuencia
          
          def mostrar(self):
              print("Codigo:{} Nombre:{} Cargo({}):{}".format(self.codigo,self.nombre,,self.cargoEmp.codigo,self.cargo))
              
        
cargo1 = Cargo("Docente")
emp1 = Empleado("Arianna",1000,cargo1)   
emp1.mostrar()
emp2 = Empleado("Daniel",1000,cargo1)     
emp2.mostrar()
 