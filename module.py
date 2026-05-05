password = input ("enter password:")
if len(password)>=8:
    print ("strong")
if len(password)>=9:
    print ("good")
else:
    print("weak")
