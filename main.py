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
print("Thank You...!")
print("------------------------------------------------------------------")
print()
