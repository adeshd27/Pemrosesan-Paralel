import psutil
import os

print('Penggunaan CPU :', psutil.cpu_percent(interval=2),'%')
print('Memori Terpakai :', psutil.virtual_memory().percent,'%')
print('memori Tersedia :', psutil.virtual_memory().available*100/psutil.virtual_memory().total,'%')

print('RX =')
print(os.popen('ifconfig|grep RX').readlines())
print('TX =')
print(os.popen('ifconfig|grep TX').readlines())