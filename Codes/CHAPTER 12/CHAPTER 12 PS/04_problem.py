try:
    def devider(u:float,v:float) ->float:
        division=u/v
        return print(division)
    devider(u=float(input("Enter numerator")),v=float(input("denominator")))
except ZeroDivisionError as e:
    print(f"You are not supposed to choose denominator as Zero,{e}")
