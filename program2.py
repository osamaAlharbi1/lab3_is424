numList = list()
for i in range(10):
    num = int(input('inter a number: '))
    numList.append(num)
max = 0
for num in numList:
    if num > max:
        max = num

print(max)