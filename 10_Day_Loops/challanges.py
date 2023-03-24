# Challenge 1: Write a Python program to print all the even numbers from 1 to 100.
for num in range(1, 101):
    if num % 2 == 0:
        print(num)


# Challenge 2: Sum of a List
numbers = [1, 2, 3, 4, 5]
sum = 0

for num in numbers:
    sum += num

print("The sum of the numbers is:", sum)

# Challenge 3: Write a Python program to find the factorial of a given number.
# Solution
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)


# Challenge 4: Write a Python program to print the multiplication table of a given number.
# Solution
num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Challenge 5: Write a Python program to find the largest element in a list.
# Solution
numbers = [5, 7, 3, 9, 1]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest element in the list:", largest)


