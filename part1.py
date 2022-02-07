print("answer to part1")

# making a dictionary
firstString = "abcdefghijklmnopqrstuvwxyz"
secondString = "cdefghijklmnopqrstuvwxyzab"
string = ""
dic = string.maketrans(firstString, secondString)

string = input("enter encrypted line: ")
answer = string.translate(dic)
print(answer)

# Change map to ocr to reach next stage
