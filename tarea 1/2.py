Estudiantes = [
    ("Carlos Rivera", 26, 100),
    ("Eduardo Rivera", 29, 90),
    ("Katia Rivera", 32, 80)
]
#print(Estudiantes)
#print(type(Estudiantes))
for Estudiante in Estudiantes:
    Nombre = Estudiante[0]
    Calificacion = Estudiante[2]
    print(f"Nombre: {Nombre}, Calificación: {Calificacion}")

Calificaciones = 0
Estudiantes3 = len(Estudiantes)

for Estudiente in Estudiantes:
    Calificaciones += Estudiante[2]

Promedio = Calificaciones / Estudiantes3
print(f"El promedio es: {Promedio}")