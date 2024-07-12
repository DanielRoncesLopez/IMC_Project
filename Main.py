import CalculadoraIMC

class Main(): 
    persona = CalculadoraIMC.CalculadoraIMC()
    persona.IngresoDatosDelUsuario()
    imc = persona.CalculoDeIMC(persona.peso, persona.estatura)
    clasificacion = persona.ClasificacionIMC(imc)
    persona.ImprimirDatosUsuario(persona.nombre, persona.apellidoPaterno, persona.apellidoMaterno, 
                                 persona.edad, persona.peso, persona.estatura, imc, clasificacion)