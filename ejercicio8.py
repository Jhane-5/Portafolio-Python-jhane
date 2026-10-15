nombre = input("Cuál es tu nombre")
edad = input("Cuál es tu edad")
nota1 = float(input("Nota1:, "))
nota2 = float(input("Nota2:, "))
nota3 = float(input("Nota3:, "))
print(" nota1,nota2,nota3")
promedio = (nota1 + nota2 + nota3) /3
resultado = promedio 
if resultado>=71:
   print("Estudiante:", nombre, "con la edad de:", edad, "obtuvo un promedio de:", resultado, "Aprobado")
else:
    print("Estudiante:", nombre, "con la edad de:", edad, "obtuvo un promedio de:", resultado, "No aprobado")

    