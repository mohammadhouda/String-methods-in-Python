numbers = [3, 5, 2, 8, 6, 1, 4, 7]

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(find_max(numbers))
# 1. Find Maximum Number
# Write a function that takes a list of numbers
# and returns the largest number without using max().
def count_occurrences(list, target):
    count = 0
    for item in list:
        if item == target:
            count += 1
    return count
print(count_occurrences(list, target))
# 2. Count Occurrences
# Write a function that takes a list and a target value,
# and returns how many times the target appears in the list.


# 3. Prime Numbers in a List
# Write a function that takes a list of numbers
# and returns a new list containing only the prime numbers
def filter_primes(numbers):
    primes = []
    for num in numbers:
        if num is < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes