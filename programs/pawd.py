import random
from string import punctuation

password=''

for i in range(2):
    special_chars = list(punctuation)
    alpha_upper = chr(random.randint(65, 90)).upper()
    alpha_lower = chr(random.randint(65, 90)).lower()
    special_symbol = special_chars[random.randint(0, 31)]
    number = random.randint(0, 9)
    password = password+alpha_upper + alpha_lower + special_symbol + str(number)

print(password)

new_password=''.join(random.sample(password,len(password)))
print(new_password)