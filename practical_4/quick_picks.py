import random
number_of_lines = int(input("Enter how many quick picks you want: "))
number = 0
for lines in range(0, number_of_lines):
    numbers = []
    list_has_values = False
    index = 0
    for current_number in range(0, 6):
        new_number = random.randrange(1, 49)
        if list_has_values is True:
            for number in numbers:
                test = number
                while len(numbers) != current_number:
                    while new_number == number:
                        new_number = random.randrange(1, 49)
                    if new_number > number:
                        numbers.insert(index+1, new_number)
                    elif new_number < number:
                        numbers.insert(index-1, new_number)
                    index += 1
                    break
        else:
            numbers.append(new_number)
            list_has_values = True
            index += 1
    print(numbers)