items = 10 #Entero
price = 2.3 #Float

total_price = items * price

print(total_price)

student_grade = [9.1, 8.8, 7.5] #Lista 
student_grades = [9, "Hello", 7.5] #Lista 

print(student_grades * 3) # Es la misma lista, repetida tres veces

print(student_grade + student_grades)

student_notes = list(range(0,11,2)) #Convertimos en rango en una lista iterable.

print(student_notes)


mysum = sum(student_grade)
length = len(student_grade)
mean = mysum / length

print(mean)

notas_estudiantes = {"Marry": 9.1, "Sim": 8.8, "John": 7.5} # tipo Dictionari
monday_temperatures = [9.1, 8.8, 7.5] # Tipo List

print(notas_estudiantes.values())  #Imprime todos los valores casi como una lista, no es exactamente una lista.
print(notas_estudiantes.keys())  #Imprime todos los valores casi como una lista, no es exactamente una lista.
print(notas_estudiantes["John"])


