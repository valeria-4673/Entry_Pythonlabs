historico = {}

while True:
    dia = input("Escriba el día de la semana: ")

    if dia == "":
        break

    temp = int(input("Escriba la temperatura: "))

    if dia in historico:
        historico[dia].append(temp)
    else:
        historico[dia] = [temp]

for dia in historico.keys():
    total_temperatures_day = sum(historico[dia])
    prom = round((total_temperatures_day/len(historico[dia])), 2)
    print("la temperatura promedio de los", dia, "fue", prom)
