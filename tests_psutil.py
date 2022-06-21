import psutil

# CPU
print(psutil.cpu_times(percpu=False))
print(psutil.cpu_times())
print(psutil.cpu_times_percent(interval=None, percpu=False))
print(psutil.cpu_count(logical=True))
# print(len(psutil.Process().cpu_affinity()))
print(psutil.cpu_stats())
print(psutil.cpu_freq(percpu=False))
print(psutil.getloadavg())

# MEMORY
print(psutil.virtual_memory())
print(psutil.swap_memory())

# DISK
print(psutil.disk_partitions(all=False))
print(psutil.disk_usage("/System/Volumes/Data"))

