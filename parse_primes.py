primes_file = open("primes.txt", "r")
primes = []
for line in primes_file:
    primes_row = line.split(" ")
    del primes_row[0]
    del primes_row[-1]
    primes += primes_row
new_primes_file = open("primes_mod.txt", "w")
for prime in primes:
    new_primes_file.write(str(prime)+"/")
print("Task complete")

from os import system
if input("cat primes_mod.txt? (yes/no) ").lower() == 'yes': system("cat primes_mod.txt") 
