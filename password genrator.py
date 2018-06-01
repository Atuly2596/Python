import random
np = int(input("Enter number of passwords")) # taking input from user
for i in range(np):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+,./' #all possible words to form password
    password = '' 
    length = int(input("Enter length of Password :"))
    for i in range(length):
        password += random.choice(char)

    print(password)