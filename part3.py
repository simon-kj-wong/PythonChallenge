import re
print("answer to part3")
f = open("part3.txt", 'r')
content = f.read()
print("".join(re.findall(r'[^A-Z+][A-Z]{3}([a-z])[A-Z]{3}[^A-Z+]', content)))
f.close()
print("take to http://www.pythonchallenge.com/pc/def/linkedlist.html")
print("which directs to http://www.pythonchallenge.com/pc/def/linkedlist.php")
