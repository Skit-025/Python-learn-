# # print(1)
# # print(2)
# # print(3)
# # print(4)
# # print(5)
# # print(6)
# # print(7)
# # print(8)
# # print(9)
# # print(10)
# #for 
# '''*
#    **
#    ***
#    ****
#    ***** 
# '''
# # for i in range(1,6):
# #         print("*" *i)


# #for
# """
#    *****
#    ****
#    ***
#    **
#    * 
# """
# # for j in range(5,0,-1):
# #         print("*"*j)
        
# """
#    *****
#     ****
#      ***
#       **
#        * 
# """

# import pyjokes
# joke=pyjokes.get_joke()
# print(joke)
# import pyttsx3
# pt=pyttsx3.init()
n=5
for i in range(0 ,n,+1):
    space=" "*(i)
    star="*"*(n-i)
    pattern=(space+star)
    print(space+star)

# pt.say(pattern)
# pt.runAndWait()
# import os
# directory_path="/"
# content=os.listdir(directory_path)
# for items in content:
#     print(items)