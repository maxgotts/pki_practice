from random import randrange
from sympy import mod_inverse

def make_mod():
	global mod, e, d
	mod = randrange(10,50)
	e = randrange(1,mod)
	try: d = mod_inverse(e, mod)
	except Exception: make_mod()
make_mod()
print(mod,"mod")
print(e,"e")
print(d,"d")
print((e*d)%mod,"== 1")
