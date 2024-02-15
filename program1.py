emp = dict()

x = 'hello'
print(x)
while(x != 'no'):

    name = input('enter the name: ')
    salary = int(input('inter the salary: '))
    emp[name] = salary
    x = input('do you want to continue: ')


print(emp)