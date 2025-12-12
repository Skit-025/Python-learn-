# n=int(input("Enter the number you wanna check :"))
# i=1
# count=0
# while(i<=n):
#     # print(i)
#     if(n%i==0):
#      count+=1
#     i+=1

# if count>2:
#         print(f"The entered number,{n} is not prime")

# else:
#         print(f"The entered number,{n} is  prime")
# # i=1
# # while(i<=10):
# #     print(i)
# #     i+=1
# i failed for for loop
# n=int(input("Enter the number you wanna check :"))

# for i in range(1,n):
#     count=0
#     if i%n==0:
#         count+=1
#     i+=1
# if count>2:
#     print("the number is not prime")
# else:
#     print("the number is  prime")

# harry bhai ka for code
n=int(input("Enter the number you wanna check :"))

for i in range(2,n):
    if n%i==0:
        print("number is not prime")
        break
else:
    print("you entered a prime number")

    









