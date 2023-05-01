numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
numbers.remove(3)
print(numbers)
print(len(numbers))


print( 1 in numbers)

#numbers.clear()
#print(numbers)

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print("Number: " +str(numbers[i]))
    i+=1
