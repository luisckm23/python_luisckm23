import clases

persona = clases.Persona()
persona.setNombre("Victor")
persona.setApellidos("Juarez")
persona.setAltura("190 cm") 
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("------------------------------------------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Abonce")
print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(f"Este metodo lo hereda del padre: {informatico.caminar()}")
print(informatico.experiencia)

print("------------------------------------------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Juan")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())