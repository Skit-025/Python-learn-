# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-1))
#     print("*"*i)
import random
import time

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}\\|;:'\",<>./?~"
length = int(input("Enter the length of the password: "))
pass1 = input("Enter your password: ")

attempts = 0
start_time = time.time()

while True:
    password = ''.join(random.choice(chars) for _ in range(length))
    attempts += 1

    if attempts % 100000 == 0:
        print(f"{attempts} attempts made... still guessing.")

    if password == pass1:
        elapsed = time.time() - start_time
        print(f"\n✅ Password guessed: {password}")
        print(f"🔁 Attempts: {attempts}")
        print(f"⏱️ Time taken: {elapsed:.2f} seconds")
        break