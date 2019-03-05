""" SET UP """
from random import choice as sample
from random import randint
from alphabet_dictionary_generator import *
from sympy import mod_inverse
import time
from json import loads


""" EXTRACT PRIMES """
primes_roto = open("primes_mod.txt", "r")
primes_pre = []
for line in primes_roto:primes = line
primes_pre = line.split("/")
del primes_pre[-1]
primes = list(map(lambda x: int(x),primes_pre))

""" MISC """
def split_by(string,index): # Stolen from StackExchange
	return [string[i * index:(i + 1) * index] for i in range((len(string) + index - 1) // index )]
def str_sum(xyz):
	bloc = ""
	for str_bloc in xyz:
		bloc += str_bloc
	return bloc

""" GENERATE PUBLIC & PRIVATE KEY """
def generateKeys():
	global P, Q, n, e, d
	P = sample(primes)
	Q = sample(primes)
	n = P*Q
	phi = (P-1)*(Q-1)
	e = sample(range(1,phi))
	try: d = mod_inverse(e, phi)
	except Exception: generateKeys()
	print((e*d)%phi,"== 1?")
	print("try: \ne", e, "\nd", d, "\nn", n,(P,Q))

""" CONVERT MESSAGE FUNCTIONS """
def convert(message):
	mssagee = ""
	for char in list(message): mssagee += alphabet[char]
	#print("convert",int(mssagee))
	return int(mssagee)
def revert(message):
	mssagee = ""
	message = str(message)
	#print("revert",message)
	if len(message)%2 != int(pre): message = pre + message
	split_message = split_by(message,2)
	for char in split_message: mssagee += reverse_alphabet[char]
	return mssagee

""" ENCODE MESSAGE FUNCTIONS """
def encode(message):
	#print("encode",int(pow(convert(message),e,n)))
	return int(pow(convert(message),e,n))
def decode(message):
	#print("decode",revert(pow(message,d,n)))
	return revert(pow(message,d,n))

""" ENCRYPT MESSAGE FUNCTIONS """
def encrypt(message):
	#print("encrypt",[encode(bloc) for bloc in split_by(message,4)])
	return str([encode(bloc) for bloc in split_by(message,4)])
def decrypt(message):
	#print("decrypt",str_sum([decode(bloc) for bloc in map(int,message)]))
	return str_sum([decode(bloc) for bloc in map(int,loads(message))])

generateKeys()

check_if_true = []
def check_if_decode_worked(message):
	if not message == decrypt(encrypt(message)): check_if_true.append(message)

x = 0
while check_if_true == []:
	running_str = ""
	length = randint(0,10000)
	for i in range(0,length): running_str += sample(extended_alphabet)
	check_if_decode_worked(running_str)
	if check_if_true == []: print("#",x,": len",length,"==>",True)
	else: print("#",x,": len",length,"==>",False)
	x += 1
print(stragglers)
print(check_if_true)
