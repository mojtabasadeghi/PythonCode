numbers = [1, 2, 5, 7, 20, 7, 8, 5, 8]

for number in numbers:
    if numbers.count(number) > 1:
        for cont in range(numbers.count(number)-1):
            numbers.remove(number)

print(numbers)
