import random

# Lista de estudiantes
estudiantes = ['David', 'Dilan', 'Anthony', 'Xonne']

# Función para generar notas aleatorias
def generar_notas(cantidad):
    return [random.randint(0, 20) for _ in range(cantidad)]

# Guardar notas de cada estudiante
notas = {}

for estudiante in estudiantes:
    notas[estudiante] = generar_notas(5)  # 5 notas aleatorias

# Mostrar resultados por estudiante
for estudiante, lista_notas in notas.items():
    promedio = sum(lista_notas) / len(lista_notas)
    nota_max = max(lista_notas)
    nota_min = min(lista_notas)

    print(f"\nResultados de {estudiante}:")
    print(f"Notas: {lista_notas}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")

    if promedio >= 18:
        print("Evaluación: Excelente 🎉")
    elif promedio >= 14:
        print("Evaluación: Bueno 🙂")
    elif promedio >= 10:
        print("Evaluación: Regular 😐")
    else:
        print("Evaluación: Necesita mejorar 😢")

# Ranking final por promedio
print("\n🏆 Ranking de estudiantes por promedio:")
ranking = sorted(notas.items(), key=lambda x: sum(x[1])/len(x[1]), reverse=True)
for i, (estudiante, lista_notas) in enumerate(ranking, 1):
    promedio = sum(lista_notas)/len(lista_notas)
    print(f"{i}. {estudiante} - Promedio: {promedio:.2f}")