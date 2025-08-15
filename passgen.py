import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_-+={[}]:'?/>.<,"
numbers = "1234567890"

upper, lower, nums, syms = True, True, True, True 

all = ""

if upper:
    all += uppercase_letters 
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols
    
length = 15
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
    


    
    
    
    
