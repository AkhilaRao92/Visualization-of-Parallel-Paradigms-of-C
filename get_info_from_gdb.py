import re

fp = open('file.txt','r')
f = open('line_num.txt','a')
g = open('locals.txt','a')

bkpt_pat = 'done,bkpt'
step_pat = 'end-stepping-range'
locals_pat = 'locals'
line_pat = 'line=\"([0-9]+)\"'
name_pat = 'name=\"([a-zA-Z]+)\"'		# () to group only the name
value_pat = 'value=\"([+-]?[0-9]+)\"'		# () to group only the value

def get_line_num(pat,sub):
	n = re.search(pat,sub)	
	if n:
		#print n.group(1)			#will have the line number as a string
		f.write(n.group(1))			#write to the file line_num.txt
		f.write('\n')

def get_locals(name_pat,val_pat,sub):
	a = re.findall(name_pat,sub)			#finds all matches in the subject
	b = re.findall(val_pat,sub)
	if a and b:
		for i in range(len(a)):
			g.write(a[i])
			g.write('=')
			g.write(b[i])
			g.write('\n')

for line in fp:
	search_bkpt = re.search(bkpt_pat,line)
	search_step = re.search(step_pat,line)
	search_locals = re.search(locals_pat,line)

	if search_bkpt:
		get_line_num(line_pat,line)
	elif search_step:
		get_line_num(line_pat,line)
	elif search_locals:
		get_locals(name_pat,value_pat,line)	

fp.close()
f.close()
g.close()
