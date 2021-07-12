#Make a program polling with dictionaries
#Make dict to save result in polling
polling = dict()
#Make list to save name for a while in polling
choose = list()

#Collect polling
while True :
    loop = input("Want to input polling?(y/n)")
    if loop == 'y':
        value = input("Input the name (Ex. Sam, Son, Sec) = ")
        choose.append(value)
    else:
        break

#Count polling
for name in choose:
    polling[name] = polling.get(name, 0) + 1

#Polling result
print("Result of polling today")
for key, count in polling.items():
    print (key, " = ", count)

