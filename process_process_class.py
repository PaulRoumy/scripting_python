import psutil
p = psutil.Process()
with p.oneshot():
    print( p.name())  # execute internal routine once collecting multiple info
    print(p.cpu_times())  # return cached value
    print( p.cpu_percent())  # return cached value
    print(p.create_time())  # return cached value
    print( p.ppid())  # return cached value
    print( p.status())  # return cached value
print(psutil.Process().ppid())
print(psutil.Process().name())
print(psutil.Process().exe())
print(psutil.Process().cmdline())
print(psutil.Process().environ())
print(psutil.Process().create_time())
print(psutil.Process().as_dict())
print(psutil.Process().parent())
print(psutil.Process().parents())
print(psutil.Process().status())
print(psutil.Process().cwd())
print(psutil.Process().username())
print(psutil.Process().terminal())
print(psutil.Process().nice())
#only linux
#print(psutil.Process().ionice())
#only linux
#print(psutil.Process().io_counters())
print(psutil.Process().num_ctx_switches())
print(psutil.Process().num_fds())
print(psutil.Process().num_threads())
print(psutil.Process().threads())
print(psutil.Process().cpu_times())
print(psutil.Process().cpu_percent())
#only linux
#print(psutil.Process().cpu_num())
#only linux
#print(psutil.Process().cpu_affinity())
print(psutil.Process().memory_info())
print(psutil.Process().memory_percent())
#linux only
#print(psutil.Process().memory_maps())
print(psutil.Process().children())
print(psutil.Process().open_files())
print(psutil.Process().connections())
print(psutil.Process().is_running())
print(psutil.Process().suspend())
print(psutil.Process().resume())
print(psutil.Process().terminate())
print(psutil.Process().kill())
print(psutil.Process().wait())

