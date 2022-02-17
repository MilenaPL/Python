# Password generator

# contains :
# from 8-20 characters
# at least 2 lowercase and 2 uppercase letters
# at least 2 digits and 2 punctuations

import random
import string

low = string.ascii_lowercase
upp = string.ascii_uppercase
pun = string.punctuation
dig = string.digits
everything = low + upp + pun + dig

random_number = random.randint(8, 20)

low_r = random.choice(low) + random.choice(low)
upp_r = random.choice(upp) + random.choice(upp)
pun_r = random.choice(pun) + random.choice(pun)
dig_r = random.choice(dig) + random.choice(dig)

everything_r = random.choice(everything) + random.choice(everything) + random.choice(everything) + random.choice(everything) + random.choice(everything) + random.choice(
    everything) + random.choice(everything) + random.choice(everything) + random.choice(everything) + random.choice(everything) + random.choice(everything) + random.choice(everything)

pass_low = []
for i in low_r:
    if len(pass_low) < 2:
        pass_low += i

pass_upp = []
for i in upp_r:
    if len(pass_upp) < 2:
        pass_upp += i

pass_dig = []
for i in dig_r:
    if len(pass_dig) < 2:
        pass_dig += i

pass_pun = []
for i in pun_r:
    if len(pass_pun) < 2:
        pass_pun += i

random_all = pass_low + pass_upp + pass_pun + pass_dig

pass_evr = random_all
for i in everything_r:
    if len(pass_evr) < random_number:
        pass_evr += i

random.shuffle(pass_evr)

ListToString = ''.join([str(elem)for elem in pass_evr])

print(f"Random password for you : {ListToString}")
