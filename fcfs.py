def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time) 
    time = 0  

    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time  

        p.waiting_time = time - p.arrival_time
        time += p.burst_time  
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
    return processes
