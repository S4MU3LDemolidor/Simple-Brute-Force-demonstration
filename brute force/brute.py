import random
import string
import time

#Defining

chars = string.ascii_letters + string.punctuation + string.digits
chars_data = list(chars)
time_now = time.strftime("%H:%M:%S")

#Input the password

password = input('Your password: ')
guess = ''
i = 0

#Initiating the brute force

while guess != password:
    guess = random.choices(chars_data, k=len(password))
    print(guess)
    guess = ''.join(guess)
    i += 1 #Guesses

#Time passed

time_after = time.strftime("%H:%M:%S")
passed_time = time.strftime("%H:%M:%S")

#Printing the password and time passed

print(f'The password is: {guess}, with a quantite of {i} of guesses.')
print(f'The brutal force started: {time_now} and ended at {time_after}')
print('This is just a simple Brute Force demonstration.')
input('To end press ENTER: ')

#End