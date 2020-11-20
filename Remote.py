from paramiko.client import SSHClient,AutoAddPolicy
from getpass import getpass
Covid77 = getpass()

sshc = SSHClient()
sshc.set_missing_host_key_policy(AutoAddPolicy())

sshconnect("10.0.2.100", 22, "rafii", Covid77)
while(True)
	sstdin, stdout, stderr = ssch.exec_command('python3 program2.py')
	print(stdout.readlines())
	print(stderr.readlines())