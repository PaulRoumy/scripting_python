import psutil

# SENSORS -> indisponible macOS
print(psutil.sensors_temperatures())
print(psutil.sensors_fans())
print(psutil.sensors_battery())


#PROCESS MANAGEMENT
print(psutil.pids())
