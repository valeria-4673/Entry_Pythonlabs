hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

def procesar():
    global mins
    global hour
    
    dura_hora = dura // 60
    dura_min = dura % 60
    
    if (dura % 60 == 0): 
        multip = int(dura / 60)
        hour += multip
        
    elif (mins + dura_min) < 60:
        hour += dura_hora
        mins += dura_min

    elif (mins + dura_min) > 60:     
        sumar_a_horas = dura // 60
        hour += sumar_a_horas
        mins = (mins + dura_min) % 60
        
def new_time():
    procesar()
    print(f'Serán las {hour}: {mins}')    
    
new_time()
