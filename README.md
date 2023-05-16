# turnaround-time-and-waiting-time-script

The following Python script utilizes data from a .txt file, exported from an operating system simulator, to calculate the average turnaround time and average waiting time for a set of processes.

Waiting time defined as: the total time spent in the READY  state (not WAITING)

Turnaround time defined as: the time at the TERMINATED state - time it first arrive in READY state
_______________________________________________________________________________________________________________________________
Sample data provided in the .txt files:

PID, STATE, MODE, START TIME, END TIME, PROGRAM

001, READY, N/A, 0000000005, 0000000040, workload/l9A.prog

001, RUNNING, USER, 0000000040, 0000000100, workload/l9A.prog

001, READY, N/A, 0000000100, 0000000105, workload/l9A.prog

001, WAITING, N/A, 0000000143, 0000000230, workload/l9A.prog

...

001, TERMINATED, N/A, 0000432536, -, workload/l9A.prog
