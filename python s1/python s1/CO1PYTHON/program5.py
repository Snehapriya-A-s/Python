n = input("Enter the limit: ")
li = []
c = 0
for i in range(n):
    x = input("Enter names: ")
    li.append(x)
for i in li:
    for j in i:
        if 'a' in j:
            c = c + 1
print("The occurence of a is: ", c)