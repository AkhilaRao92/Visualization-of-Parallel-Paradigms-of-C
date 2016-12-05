from subprocess import *
GDB_CMDLINE = 'gdb -n -q -i mi'
p1 = Popen(GDB_CMDLINE,shell=True,stdin = PIPE,stdout = PIPE,stderr = PIPE)

print p1.stdout.readline()
print p1.stdout.readline()

p1.stdin.write('-file-exec-and-symbols a.out\n')
print p1.stdout.readline()
print p1.stdout.readline()

p1.stdin.write('-break-insert main\n')
print p1.stdout.readline()

p1.stdin.write('-exec-run\n')
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()

p1.stdin.write('-exec-step\n')
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()

p1.stdin.write('-stack-list-locals 1\n')
print p1.stdout.readline()
print p1.stdout.readline()

p1.stdin.write('-exec-step\n')
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()
print p1.stdout.readline()

p1.stdin.write('-stack-list-locals 1\n')
print p1.stdout.readline()
print p1.stdout.readline()

