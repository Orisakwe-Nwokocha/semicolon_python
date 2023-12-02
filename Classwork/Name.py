name1 = "Hannah"
name2 = "Abbey"

print(name1)
print(name2)

print()

name1, name2 = name2, name1

print(name1)
print(name2)

temporary = name1
name1 = name2
name2 = temporary

print()
print(name1)
print(name2)