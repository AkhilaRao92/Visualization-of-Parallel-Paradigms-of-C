from subprocess import *

GDB_CMDLINE = 'gdb -n -q -i mi'
logfile = open('file.txt','w')

p1 = Popen(GDB_CMDLINE,shell=True,stdin = PIPE,stdout = logfile,stderr = PIPE)
raw_input("COMMAND gdb -n -q -i mi executed\nPress enter to continue")

p1.stdin.write('-file-exec-and-symbols a.out\n')
raw_input("COMMAND -file-exec-and-symbols a.out executed\nPress enter to continue")

p1.stdin.write('-break-insert main\n')
raw_input("COMMAND -break-insert main executed\nPress enter to continue")

p1.stdin.write('-exec-run\n')
raw_input("COMMAND -exec-run executed\nPress enter to continue")

for i in range(1,10):
	p1.stdin.write('-exec-step\n')
	raw_input("COMMAND -exec-step executed\nPress enter to continue")

	p1.stdin.write('-stack-list-locals 1\n')
	raw_input("COMMAND -stack-list-locals 1 executed\nPress enter to continue")


