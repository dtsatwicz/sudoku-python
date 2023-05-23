x = ['testx1']
y = ['testy1']
z = ['testz1']
def functx():
		x = 'testx2'
def functy():
		global y
		y.append('testy2')
def functz():
		global z
		z = 'testz2'
print ('a',x,y,z)
functx()
functy()
functz()
print ('b',x,y,z)
		
