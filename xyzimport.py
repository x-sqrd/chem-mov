# xyz import.py

import pprint

class Atom:
	"""
	An atom.
	"""
	def __init__(self, element, x, y, z):
		"""
		Initialise the atom.
		"""
		self.element = element
		self.x = x
		self.y = y
		self.z = z

def importMolecule(path):
	"""
	Import a molecule from a file.
	"""
	# Open the file.
	with open(path, 'r') as f:
		# Read the file.
		lines = f.readlines()
		# Get the number of atoms.
		nAtoms = int(lines[0]) +1
		# Create a list to store the atoms.
		atoms = []
		# Loop over the atoms.
		for i in range(1, nAtoms):
			# Split the line.
			line = lines[i+1].split()
			# Get the element and coordinates.
			element = line[0]
			x = float(line[1])
			y = float(line[2])
			z = float(line[3])
			# Create the atom.
			atom = Atom(element, x, y, z)
			# Add the atom to the list.
			atoms.append(atom)
			print(atom.element, atom.x, atom.y, atom.z)
	return atoms

def updateXYZ(atoms = [], x = 0, y = 0, z = 0):
	"""
	Update the coordinates of the atoms.
	"""
	for atom in atoms:
		atom.x += x
		atom.y += y
		atom.z += z
	return atoms

def printXYZ(atoms = [], path='output.xyz'):
	"""
	Print the molecule to a file.
	"""
	# Open the file.
	with open(path, 'w') as f:
		# Print the number of atoms.
		f.write(str(len(atoms)) + '\n')
		# Loop over the atoms.
		for atom in atoms:
			# Print the atom.
			f.write(atom.element + ' ' + str(atom.x) + ' ' + str(atom.y) + ' ' + str(atom.z) + '\n')

def combineNoCheck(path1, path2, output="output.xyz"):
	"""
	Combine two xyz files.
	"""
	atoms1 = importMolecule(path1)
	atoms2 = importMolecule(path2)
	atoms = atoms1 + atoms2
	printXYZ(atoms, output)
	
	# Print the molecule.

if __name__ == "__main__":
	importMolecule('test.xyz')