notebooks = int(input('How many notebooks are there'))
capacity_of_box = int(input('How many notebooks can fit in 1 box'))

#ask the user for the number of notebooks and how many books can fit in one box.

notebookin_box = (notebooks // capacity_of_box)

#To get the number of notebooks that can fit in one box you should use This code notebooks // capacity_of_box which means notebooks minus the capaccity of the box

print('number of notebooks is' , notebooks)
print('number of notebooks that can fit in one box is' , capacity_of_box)

#Add labels so your output will be cleaner

if capacity_of_box > notebooks:
    print('no full box was filled, the loose pack has' , notebooks , 'remaining notebooks')
    
#if the condition is true then the code will display this message
else:
    print('number of full boxes is' , notebooks//capacity_of_box)
    print('loose notebook is' , notebooks%capacity_of_box)
    
#the condition is false then the code will calculate the rounded qoutient and remainder of the two variables, and will display this message