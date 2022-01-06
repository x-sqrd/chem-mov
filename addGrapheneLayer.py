# addGrapheneLayer.py

global molecule 
molecule = ''
global file 
file = ''

def importFile(path):
	# X, Y, Z
	maxX = -10000.0
	maxY = -10000.0
	minX = 10000.0
	minY = 10000.0
	minZ = 10000.0 # lowest height
	with open(path, 'r') as f:
		lines = f.readlines()
		for line in lines:
			x = line.split(' ')
			while "" in x:
				x.remove("")
			# print(x)
			try:
				if float(x[1]) > maxX:
					maxX = float(x[1])
				if float(x[1]) < minX:
					minX = float(x[1])
				if float(x[2]) > maxY:
					maxY = float(x[2])
				if float(x[2]) < minY:
					minY = float(x[2])
				
				temp = x[3]
				temp.removesuffix('\n')
				if float(temp) < minZ:
					minZ = float(temp)
			except IndexError:
				pass	
	print(minX, maxX, minY, maxY, minZ)
	# now add the graphene layer under the file

if __name__ == '__main__':
	importFile('Graphene-Layer.xyz')