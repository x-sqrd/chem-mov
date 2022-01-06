from ase import *
from ase.build import bulk
from ase.visualize import view

a1 = bulk('Al', 'fcc', a=3.567)
view(a1)