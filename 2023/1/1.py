# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.


# Consider your entire calibration document. What is the sum of all of the calibration values?
from math import inf


def run_p1(input: list[str]):
    print(input)
    total_sum = 0
    for line in input:
        first_number = None
        second_number = None

        print(f'line: {line}')
        for index, char in enumerate(line):
            if char.isnumeric():
                first_number = char
                break

        # travel back the line
        for i in range(len(line) - 1, -1, -1):
            print(f'index: {i}, char: {line[i]}')
            if line[i].isnumeric():
                second_number = line[i]
                break

        print(f'for line: {line}, first_number: {first_number}, second_number: {second_number}')

        total_sum += int(first_number + second_number)

    print(f'total sum: {total_sum}')
    return total_sum


def run(input: list[str]):
    total_sum = 0

    number_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        "0": '0',
        "1": '1',
        "2": '2',
        "3": '3',
        "4": '4',
        "5": '5',
        "6": '6',
        "7": '7',
        "8": '8',
        "9": '9',
    }

    total_sum = 0
    for line in input:
        first_number = None
        second_number = None
        first_index = 999999
        second_index = 999999

        for valid_word in number_words.keys():
            if valid_word in line:
                if first_index > line.index(valid_word):
                    first_index = line.index(valid_word)
                    first_number = number_words[valid_word]

        # travel back the line
        for valid_word in number_words.keys():
            reversed_line = line[::-1]
            reversed_word = valid_word[::-1]
            if reversed_word in reversed_line:
                if second_index > reversed_line.index(reversed_word):
                    second_number = number_words[valid_word]
                    second_index = reversed_line.index(reversed_word)

        print(f'for line: {line}, first_number: {first_number}, second_number: {second_number}')

        total_sum += int(first_number + second_number)

    return total_sum
