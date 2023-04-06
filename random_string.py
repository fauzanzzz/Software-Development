import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

random_string = generate_random_string(10)
print(random_string)