marks={}
math_mark=float(input("Enter the marks secured by the student in mathematics :"))
Python_mark=float(input("Enter the marks secured by the student in python :"))
java_mark=float(input("Enter the marks secured by the student in Java :"))
marks.update({"math":math_mark})
marks.update({"python":Python_mark})
marks.update({"java":java_mark})
if(math_mark>=33):
    if(33<=math_mark<=50):
      grade="D"
      print("passed math test with Grade:",grade)

    elif(50<=math_mark<=60):
          grade="C"  
          print("passed math test with Grade:",grade)
  
    elif(60<=math_mark<=70):
         grade="B"
         print("passed math test with Grade:",grade)
    
    elif(70<=math_mark<=80):
         grade="A"
         print("passed math test with Grade:",grade)
    
    elif(80<=math_mark<=90):
          grade="E"
          print("passed math test with Grade:",grade)

    elif(90<=math_mark<=100):
         grade="O"
         print("passed math test with Grade:",grade)
#math if
else:
    if(math_mark<33):
        t=1
    print("Failed the math test")

if(Python_mark>=33):
    if(33<=Python_mark<=50):
      grade="D"
      print("passed python test with grade:",grade)

    elif(50<=Python_mark<=60):
         grade="C"  
         print("passed python test with grade:",grade)
  
    elif(60<=Python_mark<=70):
         grade="B"
         print("passed python test with grade:",grade)
    
    elif(70<=Python_mark<=80):
         grade="A"
         print("passed python test with grade:",grade)
    
    elif(80<=Python_mark<=90):
         grade="E"
         print("passed python test with grade:",grade)

    elif(90<=Python_mark<=100):
         grade="O"
         print("passed python test with grade:",grade)
#python if
else:
    if(Python_mark<33):
        t=2
    print("Failed the python test")

if(java_mark>=33):
    if(33<=java_mark<=50):
         grade="D"
         print("passed java test with Grade:",grade)

    elif(50<=java_mark<=60):
         grade="C"  
         print("passed java test with Grade:",grade)
  
    elif(60<=java_mark<=70):
         grade="B"
         print("passed java test with Grade:",grade)
    
    elif(70<=java_mark<=80):
         grade="A"
         print("passed java test with Grade:",grade)
    
    elif(80<=java_mark<=90):
         grade="E"
         print("passed java test with Grade:",grade)

    elif(90<=java_mark<=100):
         grade="O"
         print("passed java test with Grade:",grade)
#java if
else:
    if(java_mark<33):
        t=3
    print("Failed the java test")

Total=(java_mark+Python_mark+math_mark)
percentage=(Total/3)
if(40<=percentage<=50):
    grade="D"

elif(50<=percentage<=60):
    grade="C"  
  
elif(60<=percentage<=70):
    grade="B"
    
elif(70<=percentage<=80):
    grade="A"
    
elif(80<=percentage<=90):
    grade="E"

elif(90<=percentage<=100):
    grade="O"
        
if(percentage>=40 and Python_mark>=33 and math_mark>=33 and java_mark>=33):
    print("The student successfully passed the semister examination with garde:",grade)
else:
    if(t==1):
     print(f"Try again with more efforts in Math where your score was :{math_mark},\n \t Better luck next time!!!")    

print("The marks of the student are",marks)
