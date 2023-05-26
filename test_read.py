file_name = '/home/dave/flet/sudoku1.txt'

sfile= open(file_name,'r')
    
lines = sfile.readlines()

cnt=0
for line in lines:
    cnt += 1
    if (line[0] == '#'): continue
    if (line[0] == ''): continue
    line = line.strip()
    
    print (cnt, len(line), line, (not line))