class student:
    in_class=10# this is a class attribute
    section="L"# this is a class attribute
    school="SVM High School"# this is a class attribute
adi=student()
adi.in_class="B.Tech" # this is an instance attribute
print(f"in class: {adi.in_class}\n, in section: {adi.section}\n, in school: {adi.school}\n") # instance attribute is used for instant value and the class attribute is the by default value that is accepted always unless it is changed by the instance attribute.
"""Initially when python checks for an attribute, it first looks for an instance attribute.
 If it doesn't find it there, it then looks for a class attribute. 
 This allows instance attributes to override class attributes when needed, while still providing default values through class attributes."""