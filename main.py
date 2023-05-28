# python3

def parallel_processing(n, m, processing_times):
    start_times = [0] * n  #Izveido sarakstu, kas seko līdzi katras pavediena sākuma laikam
    assigned_thread = [0] * m  #Izveido sarakstu, kas seko līdzi katram uzdevumam piešķirtajam pavedienam

    for i in range(m):  #Pārbauda katru uzdevumu
        min_time = start_times[0]  #Pieņem ka minimālais sākuma laiks ir pirmā pavediena sākuma laiks
        min_thread = 0

        for j in range(1, n):  #ciklē pār atlikušajiem pavedieniem
            if start_times[j] < min_time:  #Ja pašreizējais pavediena sākuma laiks ir mazāks par pašreizējo minimālo
                min_time = start_times[j]  #Atjauno minimālo sākuma laiku
                min_thread = j  #Atjauno piešķirto pavedienu

        assigned_thread[i] = min_thread  #Piešķir uzdevumu pavedienam ar minimālo sākuma laiku

        start_times[min_thread] += processing_times[i]  #Atjauno piešķirtā pavediena sākuma laiku, pieskaitot uzdevuma apstrādes laiku

    return assigned_thread, start_times

#Izlasīt ievades vērtības n un m
n, m = map(int, input().split())

#Izlasīt uzdevumu apstrādes laikus
processing_times = list(map(int, input().split()))

#Izsaukt paralēlo apstrādes funkciju ar ievades vērtībām
assigned_thread, start_times = parallel_processing(n, m, processing_times)

#Drukāt katram uzdevumam piešķirto pavedienu un sākuma laiku
for i in range(m):
    print(assigned_thread[i], start_times[assigned_thread[i]])

