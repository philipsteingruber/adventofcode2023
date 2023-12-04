import re


def part1(input_data):
    values = []
    pattern = re.compile(r'(\d)')

    for line in input_data:
        found_digits = re.findall(pattern, line)
        digit1 = found_digits[0]
        digit2 = found_digits[-1]
        value = int(digit1+digit2)
        values.append(value)
    return sum(values)


def part2(input_data):
    values = []
    pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    translations = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in input_data:
        found_digits = re.findall(pattern, line)
        digit1 = found_digits[0]
        digit2 = found_digits[-1]
        if not str.isnumeric(digit1):
            digit1 = translations[digit1]
        if not str.isnumeric(digit2):
            digit2 = translations[digit2]
        value = int(''.join([digit1, digit2]))
        values.append(value)
    return sum(values)


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    # print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
