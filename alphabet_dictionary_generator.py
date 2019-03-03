#from pyperclip import copy
extended_alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~1!2@3£4$5%6^7&8*9(0)-_=+[{]}\|;:'\",<.>/? ")
alphabet = {}
reverse_alphabet = {}
pre, post = "0",""
for char_i in range(0,len(extended_alphabet)):
	char_v = (pre+str(char_i+1)+post)[-2] + (pre+str(char_i+1)+post)[-1]
	alphabet[extended_alphabet[char_i]] = char_v
	reverse_alphabet[char_v] = extended_alphabet[char_i]

#copy("alphabet = "+str(alphabet)+"\nreverse_alphabet = "+str(reverse_alphabet))