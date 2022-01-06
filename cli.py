

print("Importing packages...")

import pprint
from xyzimport import *
import colorama
from colorama import Fore, Style

print("\n\n\n......................")
print("..                  ..")
print("..   UnikornSuite   ..")
print("..                  ..")
print("......................")
print("\n\nBy Ayush Nayak")

input(Fore.GREEN+ "\n\nPress Enter to continue...")

print("Select the file to import:")
path = ""
while True:
	try:
		path = input(Fore.WHITE + "\n\nFile: ")
		file = path.strip()
		file = open(file, "r")
		break	
	except:
		print(Fore.RED +"\nFile not found.")

print(Fore.BLUE + "Select Operation: [1] = Update XYZ, [2] = Merge XYZ")
item = "0"
while True:
	x = input(Fore.WHITE + "> ") 
	if(x == "1" or x == "2"):
		item = x
		break
if(x == "1"):
	X = input("Amount to update x by > ")
	Y = input("Amount to update y by > ")
	Z = input("Amount to update z by > ")
	print("\n\nUpdating XYZ...")
	molecule = importMolecule(path)
	molecules = updateXYZ(molecule, float(X), float(Y), float(Z))
	print("\n\nSaving...")
	printXYZ(molecules, "output.xyz")
	