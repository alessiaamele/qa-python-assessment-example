def EndsPy(input):
    if input[-2]=="p" and input[-1]=="y":
        return True
    else:
        return False

print(EndsPy("endsinpy"))
