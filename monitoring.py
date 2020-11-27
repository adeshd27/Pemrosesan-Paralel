def monitoring():
  import psutil
  from time import sleep
  
  tx = psutil.net_io_counters().bytes_sent
  rx = psutil.net_io_counters().bytes_recv
  sleep(1)
  tx_new = psutil.net_io_counters().bytes_sent
  rx_new = psutil.net_io_counters().bytes_recv
  rx = operasi(rx, rx_new)
  tx = operasi(tx, tx_new)
  
  cpu = round(psutil.cpu_percent(interval=1), 2)
  memory = psutil.virtual_memory().percent
 
  print('''
              		MONITORING
                    CPU   : {}%
                    Memori: {}%
                    tx/rx : {} Kbps/{} Kbps'''.format(cpu, memory, tx, rx))

def operasi(old, new):
  new = new - old
  new = (new * 8) / 1000
  return round(new, 2)
  
  
monitoring()