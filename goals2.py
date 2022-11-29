#create an empty list
goals = []

#append the goals
n = int(input("How many goals do you want? "))
for i in range(5):
    new = imput("add a new goals tothe list: ")
    goals.append(new)

print(goals)
#edit an iten
i = input('Which goals do you want to chage? ')
# convert i fro m string to the integer
i = int(i)
goals[i-1] = input('Enter a new goal: ')

print(goals)

#delete an item
i = int(input('Which goals do you want to delete? '))
del goals[i-1]
print(goals)