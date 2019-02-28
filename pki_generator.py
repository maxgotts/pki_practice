""" SET UP """
P = 0
Q = 0
e = 0
n = 0
d = 0
def phi(P,Q): return (P-1)*(Q-1)

from random import choice as sample

""" EXTRACT PRIMES """
primes_roto = open("primes_mod.txt", "r")
primes_pre = []
for line in primes_roto:primes = line
primes_pre = line.split("/")
del primes_pre[-1]
primes = list(map(lambda x: int(x),primes_pre))
#print(primes)

""" GENERATE PUBLIC & PRIVATE KEY """
def generateKeys():
	P = sample(primes)
	Q = sample(primes)
	print((P,Q))
	n = P*Q
	e = sample(range(1,phi(P,Q)))
	d = (2*phi(P,Q)+1)/float(e)
	print((n,e,d))

generateKeys()

""" ALPHABET DICTIONARIES """
alphabet = {'a': '10', 'b': '20', 'c': '30', 'd': '40', 'e': '50', 'f': '60', 'g': '70', 'h': '80', 'i': '90', 'j': '100', 'k': '110', 'l': '120', 'm': '130', 'n': '140', 'o': '150', 'p': '160', 'q': '170', 'r': '180', 's': '190', 't': '200', 'u': '210', 'v': '220', 'w': '230', 'x': '240', 'y': '250', 'z': '260', 'A': '270', 'B': '280', 'C': '290', 'D': '300', 'E': '310', 'F': '320', 'G': '330', 'H': '340', 'I': '350', 'J': '360', 'K': '370', 'L': '380', 'M': '390', 'N': '400', 'O': '410', 'P': '420', 'Q': '430', 'R': '440', 'S': '450', 'T': '460', 'U': '470', 'V': '480', 'W': '490', 'X': '500', 'Y': '510', 'Z': '520', '`': '530', '~': '540', '1': '550', '!': '560', '2': '570', '@': '580', '3': '590', '£': '600', '4': '610', '$': '620', '5': '630', '%': '640', '6': '650', '^': '660', '7': '670', '&': '680', '8': '690', '*': '700', '9': '710', '(': '720', '0': '730', ')': '740', '-': '750', '_': '760', '=': '770', '+': '780', '[': '790', '{': '800', ']': '810', '}': '820', '\\': '830', '|': '840', ';': '850', ':': '860', "'": '870', '"': '880', ',': '890', '<': '900', '.': '910', '>': '920', '/': '930', '?': '940', ' ': '950'}
reverse_alphabet = {'10': 'a', '20': 'b', '30': 'c', '40': 'd', '50': 'e', '60': 'f', '70': 'g', '80': 'h', '90': 'i', '100': 'j', '110': 'k', '120': 'l', '130': 'm', '140': 'n', '150': 'o', '160': 'p', '170': 'q', '180': 'r', '190': 's', '200': 't', '210': 'u', '220': 'v', '230': 'w', '240': 'x', '250': 'y', '260': 'z', '270': 'A', '280': 'B', '290': 'C', '300': 'D', '310': 'E', '320': 'F', '330': 'G', '340': 'H', '350': 'I', '360': 'J', '370': 'K', '380': 'L', '390': 'M', '400': 'N', '410': 'O', '420': 'P', '430': 'Q', '440': 'R', '450': 'S', '460': 'T', '470': 'U', '480': 'V', '490': 'W', '500': 'X', '510': 'Y', '520': 'Z', '530': '`', '540': '~', '550': '1', '560': '!', '570': '2', '580': '@', '590': '3', '600': '£', '610': '4', '620': '$', '630': '5', '640': '%', '650': '6', '660': '^', '670': '7', '680': '&', '690': '8', '700': '*', '710': '9', '720': '(', '730': '0', '740': ')', '750': '-', '760': '_', '770': '=', '780': '+', '790': '[', '800': '{', '810': ']', '820': '}', '830': '\\', '840': '|', '850': ';', '860': ':', '870': "'", '880': '"', '890': ',', '900': '<', '910': '.', '920': '>', '930': '/', '940': '?', '950': ' '}

""" CONVERT MESSAGE FUNCTIONS """
def convert(message):
	mssagee = ""
	for char in list(message): mssagee += alphabet[char]
	return mssagee
def revert(message):
	mssagee = ""
	split_message = message.split('0')
	del split_message[-1]
	for char in split_message: mssagee += reverse_alphabet[char+'0']
	return mssagee

""" ENCODE MESSAGE FUNCTIONS """
def encode(message):
    print(e,n,message) 
    return int(convert(message))**e%n
def decode(message):
    print(d,n,message) 
    return revert(message**d%n)

xyz = input('==> ')
print(encode(xyz))
print(decode(encode(xyz)))
