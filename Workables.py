import matplotlib.pyplot as plt
num = int(input("Enter the lenght of values of the x-axis: "))
list = []
#taking inputs for the x-axis
for i in range(num):
    elements = int(input("Enter the Numbers: "))
    list.append(elements)
print("\nThe Numbers of the x-axis are: ",list)

print("\nThe lenght of values of the y-axis is: ",num)
list2 = []
#taking inputs for the x-axis
for i in range(num):
    elements2 = int(input("Enter the Numbers: "))
    list2.append(elements2)
print("\nThe Numbers of the y-axis are: ",list2)
x = list
y = list2
title = input("\nEnter the Graph Title ")
x_axis = input("\nEnter the name of the x-axis(horizontal) ")
y_axis = input("\nEnter the name of the y-axis(horizontal) ")
plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.plot(x,y)
plt.show()

