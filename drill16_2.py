from sys import argv

script, filename = argv

print('#' * 15)
print(f"I want to read the content of {filename}")
text = open(filename)
print(text.read())

text.close()