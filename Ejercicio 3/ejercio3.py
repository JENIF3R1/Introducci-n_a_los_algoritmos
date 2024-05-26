"""EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos."""

partidosGanados = int(input("Ingresar cantidad de partidos ganados: "))
partidosEmpatado = int(input("Ingresar cantidad de partidos empatados: "))
partidoPerdido = int(input("Ingresar cantidad de patidos perdidos: "))


puntosAcumulados = (partidosGanados * 3) + (partidosEmpatado * 1) + (partidoPerdido * 0)

print("Puntos acumulados del equipo en el campeonato: ", puntosAcumulados)
