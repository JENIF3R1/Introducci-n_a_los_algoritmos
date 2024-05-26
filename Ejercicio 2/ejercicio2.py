"""EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared."""

costoPorMetro2 = int(input("Ingresar costoPormetro2: "))

alto = int(input("Ingresar alto de pared: "))
ancho = int(input("Ingresar ancho de pared: "))


supercie = alto * ancho


costoTotal = costoPorMetro2 * supercie

print("El costo de mano de obra para pintar la pared:", costoTotal)
