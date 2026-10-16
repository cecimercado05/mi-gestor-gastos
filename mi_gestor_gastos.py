
# mi_gestor_gastos.py

# 1. Guardar varios gastos en una lista
gastos = [12.50, 25.00, 8.75, 32.00, 15.00, 18.50]

# 2. Calcular el total de los gastos
total = sum(gastos)

# 3. Calcular el gasto medio
media = total / len(gastos)

# Mostrar los resultados
print("=== MI GESTOR DE GASTOS ===")
print(f"Gastos registrados: {gastos}")
print(f"Total de gastos: {total:.2f} €")
print(f"Gasto medio: {media:.2f} €")

# 4. Mostrar los gastos superiores a 20 €
print("\nGastos superiores a 20 €:")

hay_gastos_mayores = False

for gasto in gastos:
    if gasto > 20:
        print(f"- {gasto:.2f} €")
        hay_gastos_mayores = True

if not hay_gastos_mayores:
    print("No hay gastos superiores a 20 €.")

# 5. Comprobar el presupuesto semanal
presupuesto = 100

print("\n=== PRESUPUESTO SEMANAL ===")
print(f"Presupuesto: {presupuesto:.2f} €")

if total > presupuesto:
    print("Has superado el presupuesto semanal.")
elif total < presupuesto:
    print(f"Te quedan {presupuesto - total:.2f} € de presupuesto.")
else:
    print("Has gastado exactamente tu presupuesto semanal.")
