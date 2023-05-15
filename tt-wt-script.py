import statistics


def get_average_turnaround_time(file_contents):
    current_pid = 0

    actual_start_times = []
    terminated_times = []

    for line in file_contents:
        pid, state, _, start_time, _, _ = line.strip().split(', ')

        pid = int(pid)
        start_time = int(start_time)

        if pid != current_pid:
            current_pid = pid
            actual_start_times.append(start_time)
            
        elif state == 'TERMINATED':
            terminated_times.append(start_time)

    turnaround_times = []
    for index, time in enumerate(actual_start_times):
        turnaround_times.append(terminated_times[index] - time) 

    average_turnaround_time = round(statistics.mean(turnaround_times), 2)

    return average_turnaround_time

def get_average_waiting_time(file_contents):

    average_waiting_time = -1

    return average_waiting_time


file_name = 'FCFS_5_20.txt'

with open(file_name, 'r') as file:
    # skip header line
    next(file)
    file_contents = file.readlines()

average_turnaround_time = get_average_turnaround_time(file_contents)
average_waiting_time = get_average_waiting_time(file_contents)

print("Average turnaround time for", file_name, "is:", average_turnaround_time)
print("Average waiting time for", file_name, " is:", average_waiting_time)