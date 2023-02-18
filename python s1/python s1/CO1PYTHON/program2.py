list = [-4, 20, 0, -13, 15, 18]
print(list)
newlist = [x for x in list if x > 0]
print("The positive numbers are: ", newlist)


n = int(input("Enter the number of numbers:"))
list = []
for i in range(n):
    a = int(input("Enter the number:"))
    list.append(a)
print(list)
list1 = [x ** 2 for x in list]
print(list1)



