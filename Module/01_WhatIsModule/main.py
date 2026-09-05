# import = imports the module (file), so we can use the things inside it.
# from = imports a specific function, variable, or class from the module.
import hello as h

import math as m

from math import pow as p
from math import sqrt as s

from calculator import add as a,multiply as m
from hello import pas as cas

from hello import student as st, course as cos, qavv as q

from message import welcome as wel, study as stt
wel()
stt()

print(st)
print(cos)
q()
# Variable → use print(variable)
# Function → use function()

# Use h. when importing the whole module: import hello as h
# Don't use h. when importing only a function: from hello import pas as p
cas()
h.introduce()

print(a(10,5))

print(m(11,5))

print(p(5,2))

print(s(36))

