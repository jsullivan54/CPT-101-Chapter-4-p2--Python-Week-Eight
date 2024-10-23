#In mathematics, the notation n\ represents the factorial of the nonnegative integer n. The factorial of n is the product of all the nonnegative integers from 1 to n. For example,
       # 7! = 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5,040
      #  and
       # 4! = 1 × 2 × 3 × 4 = 24
       # Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that number. Display the factorial.”
total = 1
num_to_factor = int(input('Please enter the number to factor: '))
for factor in range(1,num_to_factor+1):
    total *= factor
print(f'{num_to_factor} factorial is equal to: {total}')
