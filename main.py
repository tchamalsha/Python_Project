name = input("Enter your name: ")
name = name.strip()
letters = len(name)
firstLetter = name[0]
lastLetter = name[letters-1]
print()
print("------------------------------------------------------------------")
print("Your name is",name+".")
print("Your name has",letters,"Charactors.")
print("Your name is started with","'"+firstLetter+"'"," and ends with","'"+lastLetter+"'.")
print()
print("printing the frequency")
print()
i=0
r=1
n=1
while i<letters:
    while n<letters:
        if name[i]==name[n]:
            r=r+1
        n=n+1
    print(name[i],"=>",r)
    print()
    i=i+1
    r=0
    n=0
print()
print("Thank You...!")
print("------------------------------------------------------------------")
print()
