# import = imports the module (file), so we can use the things inside it.
# from = imports a specific function, variable, or class from the module.
import hello as h

import math as m

from math import pow as p
from math import sqrt as s
from calculator import add,multiply

h.introduce()

print(add(10,5))

print(multiply(11,5))

print(p(5,2))

print(s(36))
