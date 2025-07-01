# First-Come, First-Served (FCFS) Scheduling
# This is the simplest CPU scheduling algorithm
# This algorithm takes in a list of processes, sorts by arrival times, and completes each process before moving on to the next

def fcfs(processes): # processes is a given list containing the process id, arrival time, and burst time
  processes.sort(key = lambda x: x.arrival_time) # sorts the processes list by arrival times
  time = 0 # variable to track the current time

  for process in processes: 
    if time < process.arrival_time:
      time = process.arrival_time # time variable jumps to the next arrival time to simulate idle CPU time efficiently

    # Computes the waiting time, completion time, and turnaround time for the process
    # See terms.md for explanations of the variables
    # Keep in mind that arrival time and burst time are given
    process.waiting_time = time - process.arrival_time 
    time += process.burst_time
    process.completion_time = time
    process.turnaround_time = process.completion_time - process.arrival_time
  return processes
