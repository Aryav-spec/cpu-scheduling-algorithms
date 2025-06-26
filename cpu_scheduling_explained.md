# CPU Scheduling Algorithms in Python

## 🧠 Why did I do this?
I created this project to learn how different CPU scheduling algorithms work under the hood. Scheduling is a huge part of how different operating systems manage processes, and I wanted to go beyond just the theory and actually implement these algorithms in Python.

The algorithms that I have implemented so far are:
- First Come First Serve (FCFS)
- Round Robin (RR)
- Shortest Job First (SJF)
- Shortest Remaining Time First (SRTF)
- Preemptive Priority Scheduling
- Non-Preemptive Priority Scheduling

## ❓What is CPU Scheduling?
When multiple programs (or processes) are running, each CPU core is only able to handle one process (or thread) at a time. The operating system decides which process to run and on which core to run it on, as well as when to run the process. On a single-core system, the operating system switches between tasks so rapidly to the point where it gives an illusion of multitasking. On multi-core systems, the OS can run processes in parallel.

The CPU Scheduler decides which process to run next using goals like:
- Keep the CPU at max utilization
- Make users wait for as little as possible
- Be fair and predictable

There are two main types of scheduling:
- Non-preemptive: Once a process starts to run, it keeps running until it's over
- Preemptive: A process can be stopped if one with a higher priority arrives
