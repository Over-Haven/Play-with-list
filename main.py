L= [4, 1, 0, 2, 6, 3, 12, 8, 15] 

print("Original List:", L)

#variable to store the sum of # the list

count = 0

# Finding the sum

for i in L:

    count += i

#divide the total elements by

#number of elements

avg = count/len(L)

print("sum =", count)

print("average = ", avg)

#Sorting the elements of the list

L.sort()

#printing the first element

print("Smallest element is:", L[0])

#printing the last element

print("Largest element is:", L[-1])