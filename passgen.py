# Very_basic_password_generator_in_python

import string
import random


# Get the length of password from user

passlen = int(input('Enter the length of the password:'))

# Get Alphabets Digits And Punctuation using python

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.punctuation
s4 = string.digits

# Now joining all the string in one Array

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

# Now we will generate the password using random.shuffle

random.shuffle(s)
print(''.join(s[0:passlen]))
