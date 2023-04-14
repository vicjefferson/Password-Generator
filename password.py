import random

lower   = 'abcdefghijklmnopqrstuvwxyz'
upper   = lower.upper()
numbers = '123456789'
symbols = '-_=+!@#$%()'
allpass = lower + upper + symbols + numbers

password = ''

for i in range(10):
    password = ''.join([password, random.choice(allpass)])

print(password)

