class CalculadoraIMC():
    #Este metodo solicita y almacena los datos del usuario en una variable diferente segun corresponda.
    def IngresoDatosDelUsuario(self):
        self.nombre = ""
        self.apellidoPaterno = ""
        self.apellidoMaterno = ""
        self.edad = 0
        self.peso = 0
        self.estatura = 0
        while not self.nombre:
            try:
                self.nombre = str(input("Ingrese su nombre(s): "))
                if not self.nombre:
                    print('Este dato no puede quedar vacio')
                _ = float(self.nombre)
                print("Ingrese un nombre valido")
                self.nombre = ""
            except:
                pass
        while not self.apellidoPaterno:
            try: 
                self.apellidoPaterno = str(input("Ingrese su apellido paterno: "))
                if not self.apellidoPaterno:
                    print('Este dato no puede quedar vacio')
                _ = float(self.apellidoPaterno)
                print("Ingrese un apellido valido")
                self.apellidoPaterno = ""
            except:
                pass
        while not self.apellidoMaterno:
            try: 
                self.apellidoMaterno = str(input("Ingrese su apellido materno: "))
                if not self.apellidoMaterno:
                    print('Este dato no puede quedar vacio')
                _ = float(self.apellidoMaterno)
                print("Ingrese un apellido valido")
                self.apellidoMaterno = ""
            except:
                pass
        while not self.edad:
            try: 
                self.edad = int(input("Ingrese su edad: "))
                if not self.edad:
                    print('Este dato no puede quedar vacio')
            except:
                print("Ingrese una edad valida")
        while not self.peso:
            try:
                self.peso = float(input("Ingrese su peso en kilogramos: "))
                if not self.peso:
                    print('Este dato no puede quedar vacio')
            except:
                print("Ingrese un peso valido")
        while not self.estatura:
            try:
                self.estatura = float(input("Ingrese su estatura en metros: "))
                if not self.estatura:
                    print('Este dato no puede quedar vacio')
            except:
                print("Ingrese una altura valida")

    #Este metodo calcula el IMC indice de masa corporal.
    def CalculoDeIMC(self, peso, estatura):
        imc = peso/pow(estatura, 2)
        return imc
    
    #Este metodo clasifica el IMC
    def ClasificacionIMC(self, imc):
        if imc <= 18.5:
            clasificacion = "Peso bajo"
        if imc > 18.5 and  imc <= 24.9:
            clasificacion = "Peso normal"
        if imc > 25 and  imc <= 29.9:
            clasificacion = "Sobrepeso"
        if imc > 30 and  imc < 34.9:
            clasificacion = "Obesidad I"
        if imc > 35 and  imc < 39.9:
            clasificacion = "Obesidad II"
        if imc > 40:
            clasificacion = "Obesidad III"
        return clasificacion

    #Este metodo imprime los valores introducidos en el metodo IngresoDatosDelUsuario()
    def ImprimirDatosUsuario(self, nombre, apellidoPaterno, apellidoMaterno, edad, peso, estatura, imc, clasificacion):
        print("*****************************************************************************")
        print("****************************   RESULTADOS  **********************************")
        print("*****************************************************************************")
        print("Nombre del Usuario:   " + nombre +" "+ apellidoPaterno +" "+ apellidoMaterno)
        print("Edad:                 %s años" %edad)
        print("Peso:                 %s kilogramos" %peso)
        print("Altura:               %s metros" %estatura)
        print("IMC:                  %s" %(imc))
        print("Clasificacion =       " + clasificacion)
