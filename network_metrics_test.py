import psutil
import logging
#Network
print(psutil.net_io_counters(pernic=False, nowrap=True))
#indisponible MacOs
#print(psutil.net_connections(kind='inet4'))
print(psutil.net_if_addrs())
print(psutil.net_if_stats())