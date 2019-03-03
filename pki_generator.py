""" SET UP """
from random import choice as sample
from alphabet_dictionary_generator import pre,post,alphabet,reverse_alphabet
from sympy import mod_inverse


""" EXTRACT PRIMES """
primes_roto = open("primes_mod.txt", "r")
primes_pre = []
for line in primes_roto:primes = line
primes_pre = line.split("/")
del primes_pre[-1]
primes = list(map(lambda x: int(x),primes_pre))

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

""" ALPHABET DICTIONARIES (imported now)
alphabet =  {'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', 'A': '27', 'B': '28', 'C': '29', 'D': '30', 'E': '31', 'F': '32', 'G': '33', 'H': '34', 'I': '35', 'J': '36', 'K': '37', 'L': '38', 'M': '39', 'N': '40', 'O': '41', 'P': '42', 'Q': '43', 'R': '44', 'S': '45', 'T': '46', 'U': '47', 'V': '48', 'W': '49', 'X': '50', 'Y': '51', 'Z': '52', '`': '53', '~': '54', '1': '55', '!': '56', '2': '57', '@': '58', '3': '59', '£': '60', '4': '61', '$': '62', '5': '63', '%': '64', '6': '65', '^': '66', '7': '67', '&': '68', '8': '69', '*': '70', '9': '71', '(': '72', '0': '73', ')': '74', '-': '75', '_': '76', '=': '77', '+': '78', '[': '79', '{': '80', ']': '81', '}': '82', '\\': '83', '|': '84', ';': '85', ':': '86', "'": '87', '"': '88', ',': '89', '<': '90', '.': '91', '>': '92', '/': '93', '?': '94', ' ': '95'}
reverse_alphabet =  {'01': 'a', '02': 'b', '03': 'c', '04': 'd', '05': 'e', '06': 'f', '07': 'g', '08': 'h', '09': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z', '27': 'A', '28': 'B', '29': 'C', '30': 'D', '31': 'E', '32': 'F', '33': 'G', '34': 'H', '35': 'I', '36': 'J', '37': 'K', '38': 'L', '39': 'M', '40': 'N', '41': 'O', '42': 'P', '43': 'Q', '44': 'R', '45': 'S', '46': 'T', '47': 'U', '48': 'V', '49': 'W', '50': 'X', '51': 'Y', '52': 'Z', '53': '`', '54': '~', '55': '1', '56': '!', '57': '2', '58': '@', '59': '3', '60': '£', '61': '4', '62': '$', '63': '5', '64': '%', '65': '6', '66': '^', '67': '7', '68': '&', '69': '8', '70': '*', '71': '9', '72': '(', '73': '0', '74': ')', '75': '-', '76': '_', '77': '=', '78': '+', '79': '[', '80': '{', '81': ']', '82': '}', '83': '\\', '84': '|', '85': ';', '86': ':', '87': "'", '88': '"', '89': ',', '90': '<', '91': '.', '92': '>', '93': '/', '94': '?', '95': ' '}
"""

""" CONVERT MESSAGE FUNCTIONS """
def convert(message):
	mssagee = ""
	for char in list(message): mssagee += alphabet[char]
	print("message,convert",int(mssagee))
	return int(mssagee)
def revert(message):
	mssagee = ""
	message = str(message)
	print("message, revert",message)
	if len(message)%2 != int(pre): message = pre + message
	split_message = [str(message)[i:i+2] for i in range(0, len(str(message)), 2)]
	for char in split_message: mssagee += reverse_alphabet[char]
	return mssagee

""" ENCODE MESSAGE FUNCTIONS """
def encode(message):
    return int(pow(convert(message),e,n))
def decode(message):
	#print(message,d,n)
	return revert(pow(message,d,n))

generateKeys()

xyz = input('==> ')
print(xyz,"-->",decode(encode(xyz)))
