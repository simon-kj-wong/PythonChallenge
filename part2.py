from collections import Counter
print("answer to part2")
f = open("part2.txt", 'r')
content = f.read()
content.strip()

freq = Counter(content)
print(freq.most_common())
f.close()

# Change ocr to equality
