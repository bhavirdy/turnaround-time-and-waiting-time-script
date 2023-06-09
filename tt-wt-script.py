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

    waiting_times = []
    sum_current_waiting_time = 0

    for line in file_contents:
        _, state, _, start_time, end_time, _ = line.strip().split(', ')

        if state == 'TERMINATED':
            waiting_times.append(sum_current_waiting_time)
            sum_current_waiting_time = 0

        elif state == "READY":
            sum_current_waiting_time += (int(end_time) - int(start_time))

    average_waiting_time = round(statistics.mean(waiting_times), 2)

    return average_waiting_time


file_path = 'test.txt'

with open(file_path, 'r') as file:
    # skip header line
    next(file)
    file_contents = file.readlines()

average_turnaround_time = get_average_turnaround_time(file_contents)
average_waiting_time = get_average_waiting_time(file_contents)

print("Average turnaround time for", file_path, "is:", average_turnaround_time)
print("Average waiting time for", file_path, " is:", average_waiting_time)