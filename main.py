file = "hello"
chars = file.split()
poschars = [chars[0]]
print(chars)
for i in range(len(chars)):
    for j in range(len(chars)- i):
        poschars.append(poschars[-1]+chars[j+i])

print(poschars)
