extended_alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~1!2@3£4$5%6^7&8*9(0)-_=+[{]}\|;:'\",<.>/? ")
alpha = {}
ahpla = {}
for char_i in range(0,len(extended_alphabet)):
	alpha[extended_alphabet[char_i]] = str(char_i+1)+"0"
	ahpla[str(char_i+1)+"0"] = extended_alphabet[char_i]
print(alpha)
print()
print(ahpla)