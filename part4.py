import urllib.request
import re

# Create a while loop with 500 iterations starting with nothing = 44827
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'
pattern = re.compile(r'and the next nothing is (\d+)')


while True:
    with urllib.request.urlopen(url + str(nothing)) as response:
        text = response.read()
        match = pattern.search(str(text))
        if (match == None):
            break
        response.close()
        print(text)
        nothing = match.group(1)
print(url+nothing)

# Meet 16044 which is to be divided by 2

nothing = '8022'
while True:
    with urllib.request.urlopen(url + str(nothing)) as response:
        text = response.read()
        match = pattern.search(str(text))
        if (match == None):
            break
        response.close()
        print(text)
        nothing = match.group(1)
print(url+nothing)

print("directed to peak.html")
