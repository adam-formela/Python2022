def sum_number(numbers):
    counter = 0
    for num in numbers:
        counter += num

    return counter

# ----- glowna czesc skryptu:

list_of_numbers = [3, 5, 12, 11, 10]
total = sum_number(list_of_numbers)
print(total)
