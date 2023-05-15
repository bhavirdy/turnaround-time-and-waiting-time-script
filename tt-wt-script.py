with open('test.txt', 'r') as file:
    # skip header line
    next(file)
    file_contents = file.readlines()

current_pid = 0

actual_start_times = []
terminated_times = []

for line in file_contents:
    pid, state, mode, start_time, end_time, program = line.strip().split(', ')

    pid = int(pid)
    start_time = int(start_time)

    if pid != current_pid:
        current_pid = pid
        actual_start_times.append(start_time)
    elif state == 'TERMINATED':
        terminated_times.append(start_time)
    else:
        continue

turnaround_times = []
for index, time in enumerate(actual_start_times):
    turnaround_times.append(terminated_times[index] - time)

print(actual_start_times)
print(terminated_times)
print(turnaround_times)   