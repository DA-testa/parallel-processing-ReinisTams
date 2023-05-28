# python3

def parallel_processing(n, m, processing_times):
    start_times = [0] * n  
    assigned_thread = [0] * m  

    for i in range(m):
        min_time = start_times[0]
        min_thread = 0

       
        for j in range(1, n):
            if start_times[j] < min_time:
                min_time = start_times[j]
                min_thread = j

 
        assigned_thread[i] = min_thread

   
        start_times[min_thread] += processing_times[i]

    return assigned_thread, start_times



n, m = map(int, input().split())
processing_times = list(map(int, input().split()))


assigned_thread, start_times = parallel_processing(n, m, processing_times)


for i in range(m):
    print(assigned_thread[i], start_times[assigned_thread[i]])

