import random
import string

# generate 2000 random strings ofr length 12

random_string = open("random_strings.csv","wt")

def get_random_string(length):
    # choose from all lowercase letter
    letters = ['A','T','C','G']
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

for i in range(2000):
    seq = get_random_string(12)
    random_string.write(seq + ",")

random_string.close()