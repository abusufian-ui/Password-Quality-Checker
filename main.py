import string

Key = input("Enter Password: ")
Strength = 0

if len(Key) >= 8: #Check if the length is 8+ characters or not
    Strength += 20

for char in Key: #Check atleast 1 uppercase alphabet
    if char.isupper():
        Strength += 20
        break

for char in Key: #Check atleast 1 lowcase alphabet
    if char.islower():
        Strength += 20
        break

for char in Key: #Check atleast 1 Special character
    if char in string.punctuation:
        Strength += 20
        break    

for char in Key: #Check atleast 1 number
    if char.isdigit():
        Strength += 20
        break    

if 0 <= Strength <= 40:
    print("PASSWORD STRENGTH IS POOR")
elif 40 < Strength <= 60:
    print("PASSWORD STRENGTH IS FAIR")
elif 60 < Strength <= 100:
    print("PASSWORD STRENGTH IS EXCELLENT")